from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/test')
def test():
    return 'Health OK'

@app.route('/hello',methods=['POST'])
def func1():
    text = request.json
    data = text.get("text")
    data = "Hello  people ::::::  " + data
    return (data)

@app.route('/hi',methods=['POST'])
def func2():
    text = request.json
    data = text.get("text")
    return (data)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8888, debug=True)

