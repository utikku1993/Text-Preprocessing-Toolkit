from gensim.utils import deaccent

def run(payload):
    
    text = payload['text']

    if isinstance(text, str):
        text = deaccent(text)
    else:
        text = [deaccent(word) for word in text]

    payload['text'] = text

    return payload