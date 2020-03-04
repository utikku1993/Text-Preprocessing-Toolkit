import glob
from flask import Flask, request
from text_processing_pipeline import run
from os.path import dirname, basename, isfile, join

app = Flask(__name__)

@app.route("/task", methods = ['POST'])
def task_runner():
    return_value = run(request.json)
    return_value['success'] = True
    return return_value

@app.route("/list", methods = ['GET'])
def list_services():
    return_value = {}
    modules = glob.glob(join(dirname(__file__), "tools/*.py"))
    available_services = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
    return_value['services'] = available_services
    return return_value

if __name__ == "__main__":
    app.run(debug=True, port=9443)