import os
import json

def run(payload):
    contractions = {}
    with open('{}/resources/contractions.json'.format(os.getcwd()), 'r') as f:
        contractions = json.load(f)
    
    contractions = dict((k.lower(), v) for k,v in contractions.items())

    text = payload['text']

    if isinstance(text, str):
        temp_text = []
        
        for word in text.split():
            if word.lower() in contractions.keys():
                temp_text.append(contractions[word.lower()])
            else:
                temp_text.append(word)

        text = ' '.join(temp_text)

    else:
        temp_text = []
        
        for word in text:
            if word.lower() in contractions.keys():
                temp_text.append(contractions[word.lower()])
            else:
                temp_text.append(word)

        text = temp_text

    payload['text'] = text

    return payload