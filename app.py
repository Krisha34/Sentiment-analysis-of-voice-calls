import os
import pickle
import speech_recognition as sr
from flask import Flask, render_template, request, jsonify, redirect
import librosa
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the audio sentiment model
with open('models/vectorizer1.pkl', 'rb') as v:
    vectorizer = pickle.load(v)

with open('models/model1.pkl', 'rb') as m:
    text_model = pickle.load(m)

# Load the audio emotion model
audio_model = load_model('models/emotionRecognitionModelcnn150.h5')

# Define the feature extraction function for audio emotion prediction
def extract_features(data, sample_rate):
    result = np.array([])
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
    result = np.hstack((result, zcr))

    stft = np.abs(librosa.stft(data))
    chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
    result = np.hstack((result, chroma_stft))

    rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
    result = np.hstack((result, rms))

    mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mel))

    return result

# Define the function to predict sentiment from audio text
def predict_sentiment(audio_text):
    review_vector = vectorizer.transform([audio_text])
    sentiment_prediction = text_model.predict(review_vector)
    sentiment_labels = {1: 'Positive', 0: 'Neutral', -1: 'Negative'}
    sentiment_label = sentiment_labels[sentiment_prediction[0]]
    return sentiment_label

# Define the function to predict emotion from audio path
def predict_emotion(audio_path):
    data, sample_rate = librosa.load(audio_path, duration=2.5, offset=0.6)
    features = extract_features(data, sample_rate)
    features = np.expand_dims(features, axis=0)
    features = np.expand_dims(features, axis=2)
    prediction = audio_model.predict(features)
    emotion_labels = ['neutral', 'calm', 'happy', 'sad', 'angry', 'fear', 'disgust', 'surprise']
    predicted_emotion = emotion_labels[np.argmax(prediction)]
    return predicted_emotion

# Define the function to convert audio to text
def convert_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text

# Define the function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

# Define the route for predicting sentiment and emotion from text and audio
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        if 'audio' in request.files:
            # Audio file provided
            audio_file = request.files['audio']
            if audio_file.filename != '':
                # Save the audio file temporarily
                audio_path = 'temp_audio.wav'
                audio_file.save(audio_path)
                # Convert audio to text
                audio_text = convert_audio_to_text(audio_path)
                # Preprocess the audio text
                preprocessed_text = preprocess_text(audio_text)
                # Predict sentiment from audio text
                audio_sentiment = predict_sentiment(preprocessed_text)
                # Predict emotion from audio
                audio_emotion = predict_emotion(audio_path)
                # Delete the temporary audio file
                os.remove(audio_path)
                return jsonify({'transcript': preprocessed_text, 'sentiment': audio_sentiment, 'emotion': audio_emotion})


            else:
                return jsonify({'error': 'No audio file provided.'})
        else:
            return jsonify({'error': 'No audio file provided.'})

@app.route('/logout', methods=['POST'])
def logout():
    # Add any logout actions if needed
    return redirect('http://localhost/login/register.php')

if __name__ == '__main__':
    app.run(debug=True)