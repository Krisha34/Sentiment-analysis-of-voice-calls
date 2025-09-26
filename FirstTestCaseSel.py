import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Specify the path to the chromedriver executable
chromedriver_path = r"C:\Users\nikit\Downloads\chromedriver-win64\chromedriver.exe"

# Create Chrome WebDriver options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")  # You can add more options if needed

# Add the executable path directly to the PATH environment variable
import os
os.environ["PATH"] += os.pathsep + chromedriver_path

# Initialize Chrome WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://localhost/login/login.php")

# Input values
username_input = driver.find_element("id", "exampleInputEmail1")
password_input = driver.find_element("id", "exampleInputPassword1")

# Clear any pre-filled values
username_input.clear()
password_input.clear()

# Input the correct credentials
username_input.send_keys("nikita@gmail.com")
password_input.send_keys("12345678")

# Correct the element locating method for the class attribute
login_button = driver.find_element("class name", "btn-primary")  # Corrected class name

login_button.click()

# Wait for a brief moment to allow the page to load and the login process to complete
time.sleep(2)

# Check if login was successful
actTit = driver.title
exptit = "Admin login system!"

if actTit == exptit:
    print("Login fail")
else:
    print("Login success")

# Close the browser window
driver.quit()
