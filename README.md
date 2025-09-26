# 🎙️ Sentiment Analysis across Modalities

This project implements a **Sentiment Analysis system for audio recordings**, extending the ideas explored in our IEEE-published research. It supports both **live audio recording** and **audio file uploads**, and predicts:

- 📜 **Transcript** (speech-to-text)
- 🙂 **Sentiment** (positive / negative / neutral)
- 🎭 **Emotion** (e.g., happy, sad, angry, etc.)

---

## 📚 Publications

This work builds on our research contributions:

- **Sentiment Analysis across Modalities: A Comprehensive Review of Text and Audio Approaches**  
  *IEEE, 2024*  
  [Link](https://ieeexplore.ieee.org/document/10480751)

- **Exploring Dual-Module Approaches for Sentiment Analysis in Call Recordings**  
  *IEEE, 2024*  
  [Link](https://ieeexplore.ieee.org/document/10690070)

---

## 🚀 Features

- 🎤 **Record Audio** in-browser and send directly to the model
- 📂 **Upload Audio Files** (`.wav`, `.mp3`, `.m4a`) for prediction
- 🔎 **Dual-module pipeline**:
  - Automatic Speech Recognition (ASR) for transcription  
  - Sentiment + Emotion classifier using trained ML models
- 🌐 Web interface built with **Flask + JavaScript**
- ⚡ Supports quick deployment on Render, Railway, or GCP Cloud Run

---

## 🛠️ Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>/Final Project
