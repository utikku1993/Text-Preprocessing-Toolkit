from flask import Flask, request
from text_processing_pipeline import run

app = Flask(__name__)

@app.route("/task", methods = ['POST'])
def task_runner():
    return_value = run(request.json)
    return_value['success'] = True
    return return_value

if __name__ == "__main__":
    app.run(debug=True, port=9443)