from nltk.tokenize import sent_tokenize

def run(payload):

    text = payload['text']

    if isinstance(text, str):
        text = sent_tokenize(text)
    else:
        text = [sent_tokenize(para) for para in text]

    payload['text'] = text

    return payload