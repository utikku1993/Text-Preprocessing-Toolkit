import sys
import yaml
from tools import *

text_processing_pipeline = []

with open("pipeline.yml", 'r') as stream:
    try:
        text_processing_pipeline = yaml.safe_load(stream)['text_processing_pipeline']
    except yaml.YAMLError as exc:
        print(exc)

def run(payload):

    pipeline = text_processing_pipeline
    if 'pipeline' in payload.keys():
        pipeline = payload['pipeline']
    
    for step in pipeline:
        payload = eval("{}.run({})".format(step, payload))
    
    return payload


if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = {}
        payload['text'] = sys.argv[1]
        print(run(payload, None)['text'])
    else:
        raise Exception("Please Pass Text To Be Processed")