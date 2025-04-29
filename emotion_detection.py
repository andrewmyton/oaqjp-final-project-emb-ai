import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'    
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        output = formatted_response['emotionPredictions'][0]['emotion']
        output['dominant_emotion'] = max(output, key = output.get)
    
    elif response.status_code == 400:
        output = None
    
    return output