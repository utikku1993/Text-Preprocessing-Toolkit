import re

def run(payload):

    keep = []
    remove = []
    preserveSpaces = True

    if 'specialChars' in payload.keys():
        
        if 'preserveSpaces' in payload['specialChars'].keys():
            preserveSpaces = payload['specialChars']['preserveSpaces']

        if 'keep' in payload['specialChars'].keys():
            keep = payload['specialChars']['keep']

        if 'remove' in payload['specialChars'].keys():
            remove = payload['specialChars']['remove']

    text = payload['text']

    if len(keep) == 0 and len(remove) == 0:
        if isinstance(text, str):
            text = re.sub('\s+',' ',text)
            text = ''.join([char for char in text if char.isalnum() or (preserveSpaces and char == ' ')])
        else:
            text = [''.join([char for char in re.sub('\s+',' ',word) if char.isalnum() or (preserveSpaces and char == ' ')]) for word in text]

    else:
        if isinstance(text, str):
            text = ''.join([char for char in text if char in keep and char not in remove])
        else:
            text = [''.join([char for char in word if char in keep and char not in remove]) for word in text]

    payload['text'] = text

    return payload