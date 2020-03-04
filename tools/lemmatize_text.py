from nltk.stem import WordNetLemmatizer

def run(payload):
    lemmatizer = WordNetLemmatizer()
    text = payload['text']

    if isinstance(text, str):
        text = ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(text)])
    else:
        text = [lemmatizer.lemmatize(word) for word in text]

    payload['text'] = text

    return payload