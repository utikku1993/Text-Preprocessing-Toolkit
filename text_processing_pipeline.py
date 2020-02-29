import sys
import yaml
from tools import *

text_processing_pipeline = []

with open("pipeline.yml", 'r') as stream:
    try:
        text_processing_pipeline = yaml.safe_load(stream)['text_processing_pipeline']
    except yaml.YAMLError as exc:
        print(exc)

def run(payload, pipeline=None):
    if pipeline is None:
        pipeline = text_processing_pipeline
    
    for step in pipeline:
        payload = eval("{}.run({})".format(step, payload))
    
    return payload