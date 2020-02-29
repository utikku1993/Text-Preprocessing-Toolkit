import sys
from text_processing_pipeline import run

if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = {}
        payload['text'] = sys.argv[1]
        print(run(payload)['text'])
    else:
        raise Exception("Please Pass Text To Be Processed")