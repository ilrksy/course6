# Emotion Detection with Watson NLP

## Project Overview
This project is a web application that detects the emotions (anger, disgust,
fear, joy, sadness) expressed in a piece of text. It uses IBM Watson NLP's
EmotionPredict API to analyze the text and returns the dominant emotion
along with the individual emotion scores. The application is deployed as a
Flask web service with a simple HTML front end.

## Features
- Analyzes text input and returns scores for anger, disgust, fear, joy, and sadness
- Identifies the dominant emotion from the input text
- Flask-based web server with a REST endpoint (`/emotionDetector`)
- Simple web UI for entering text and viewing results
- Input validation with error handling for blank/invalid text
- Unit tests covering each emotion category
- PEP8-compliant code verified with PyLint static analysis

## Project Structure
```
.
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Requirements
- Python 3.x
- Flask
- Requests

Install dependencies:
```
pip install flask requests
```

## Running the Application
```
python3 server.py
```
Then open a browser and navigate to `http://localhost:5000`.

## Running Unit Tests
```
python3 -m unittest test_emotion_detection.py
```

## Static Code Analysis
```
pylint server.py
```

## Usage
Enter a sentence in the text box and click "Analyze" to see the emotion
scores and the dominant emotion detected in the statement.
