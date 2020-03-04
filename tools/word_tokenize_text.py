from nltk.tokenize import word_tokenize

def run(payload):

    text = payload['text']

    if isinstance(text, str):
        text = word_tokenize(text)
    else:
        text = [word_tokenize(sent) for sent in text]

    payload['text'] = text

    return payload