"""
Module for detecting emotions in text using Watson NLP.
"""
import json
import requests


def emotion_detector(text_to_analyse):
    """
    Sends text to the Watson NLP EmotionPredict API and returns a dictionary
    containing the scores for anger, disgust, fear, joy, sadness and the
    dominant emotion.

    If the input text is blank (or the service returns a 400 status code),
    all scores and the dominant_emotion are set to None.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=myobj, headers=headers, timeout=10)

    # Handle blank / invalid input which the service flags with a 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
