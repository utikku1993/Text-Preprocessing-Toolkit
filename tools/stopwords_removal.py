from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def run(payload):

    stop_words = set(stopwords.words("english"))

    if 'stopwords' in payload.keys():
        if 'lang' in payload['stopwords'].keys():
            stop_words = set()
            for lang in payload['stopwords']['lang']:
                stop_words = stop_words + set(stopwords.words(lang))
            stop_words = set(stop_words)

        if 'include' in payload['stopwords'].keys():
            stop_words = stop_words + payload['stopwords']['include']
            stop_words = set(stop_words)

        if 'exclude' in payload['stopwords'].keys():
            for word in payload['stopwords']['exclude']:
                stop_words.remove(word)

        if 'useOnly' in payload['stopwords'].keys():
            stop_words = payload['stopwords']['useOnly']

    text = payload['text']

    if isinstance(text, str):
        text = ' '.join([word for word in word_tokenize(text) if word not in stop_words])
    else:
        text = [word for word in text if word not in stop_words]

    payload['text'] = text

    return payload