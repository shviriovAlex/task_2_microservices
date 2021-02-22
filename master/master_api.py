from flask import Flask, render_template, redirect
from flask_restful import Api, Resource, request
import requests

app = Flask(__name__, template_folder='templates')
api = Api(app)


class Master(Resource):

    def __init__(self, word, link):
        self.word = word
        self.link = link

    def post(self):
        return requests.post('http://localhost:8001', json={self.word: self.link})


class MasterGetWord(Resource):

    def __init__(self, word):
        self.word = word

    def get(self):
        return requests.get(f"http://localhost:8002/{self.word}")


@app.route('/', methods=['GET', 'POST'])
def send_data():
    if request.method == 'POST':
        wordDetails = request.form
        word = wordDetails['word']
        link = wordDetails['link']
        Master(word, link).post()
        return redirect('http://localhost:8000')

    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        wordDetails = request.form
        word = wordDetails['word']
        MasterGetWord(word).get()
        return redirect(f"http://localhost:8002/{word}")

    return render_template('search.html')


api.add_resource(Master, '/')
api.add_resource(MasterGetWord, '/search')
if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
