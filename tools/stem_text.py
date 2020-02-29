
def run(payload):
    
    text = payload['text']

    if isinstance(text, str):
        text = text.lower()
    else:
        text = [word.lower() for word in text]

    payload['text'] = text

    return payload