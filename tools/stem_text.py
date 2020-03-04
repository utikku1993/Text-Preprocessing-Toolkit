from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def run(payload):
    ps = PorterStemmer()

    text = payload['text']

    if isinstance(text, str):
        text = ' '.join([ps.stem(word) for word in word_tokenize(text)])
    else:
        text = [ps.stem(word) for word in text]

    payload['text'] = text

    return payload