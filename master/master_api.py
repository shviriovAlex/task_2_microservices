from flask import Flask, render_template, url_for, redirect, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource, request
import requests

app = Flask(__name__, template_folder='templates')
api = Api(app)


class Master(Resource):

    def __init__(self, word, link):
        self.word = word
        self.link = link

    def post(self):
        return requests.post('http://127.0.0.2:5000', json={self.word: self.link})


class MasterGetWord(Resource):

    def __init__(self, word):
        self.word = word

    def get(self):
        return requests.get(f"http://127.0.0.3:5000/{self.word}")


@app.route('/', methods=['GET', 'POST'])
def send_data():
    if request.method == 'POST':
        wordDetails = request.form
        word = wordDetails['word']
        link = wordDetails['link']
        Master(word, link).post()
        return redirect('http://127.0.0.1:5000')

    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        wordDetails = request.form
        word = wordDetails['word']
        MasterGetWord(word).get()
        return redirect(f"http://127.0.0.3:5000/{word}")

    return render_template('search.html')


api.add_resource(Master, '/')
api.add_resource(MasterGetWord, '/search')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
