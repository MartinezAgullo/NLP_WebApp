import requests
import json

# Sentiment usses: positive, negative, and neutral
def sentiment_analyzer(text_to_analyse):
   url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
   myobj = { "raw_document": { "text": text_to_analyse } }
   header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
   response = requests.post(url, json = myobj, headers=header)
   formatted_response = json.loads(response.text)
   label = formatted_response['documentSentiment']['label']
   score = formatted_response['documentSentiment']['score']
   return {'label': label, 'score': score}

# Emotion uses: anger, disgust, fear, joy, and sadness
def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():  
        return None

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        max_emotion = max(emotion.items(), key=lambda x: x[1])
        return max_emotion[0]
    else:
        return None