import requests
import json

def emotion_detector(text_to_analyze):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=header, json=myobj)
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotions = response_dict['emotionPredictions'][0]['emotion']
        anger_score   = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score    = emotions['fear']
        joy_score     = emotions['joy']
        sadness_score = emotions['sadness']
    elif response.status_code == 400:
        anger_score   = None
        disgust_score = None
        fear_score    = None
        joy_score     = None
        sadness_score = None
    
    emotion_scores = {
        'anger':   anger_score,
        'disgust': disgust_score,
        'fear':    fear_score,
        'joy':     joy_score,
        'sadness': sadness_score
    }
    
    if response.status_code == 200:
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    elif response.status_code == 400:
        dominant_emotion = None

    result = {
        'anger':   anger_score,
        'disgust': disgust_score,
        'fear':    fear_score,
        'joy':     joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return result

