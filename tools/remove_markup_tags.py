from bs4 import BeautifulSoup

def run(payload):
    
    text = payload['text']

    parser = "html.parser"

    if 'parser' in payload.keys():
        parser = payload['parser']

    if isinstance(text, str):
        text = BeautifulSoup(text, parser).text
    else:
        text = [BeautifulSoup(text, parser).text for word in text]

    payload['text'] = text

    return payload