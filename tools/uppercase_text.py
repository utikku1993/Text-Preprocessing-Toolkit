
def run(payload):
    
    text = payload['text']

    if isinstance(text, str):
        text = text.upper()
    else:
        text = [word.upper() for word in text]

    payload['text'] = text

    return payload