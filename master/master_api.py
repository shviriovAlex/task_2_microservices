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
        """
        Send data from html form in Reaper
        to start parsing. Get data from function send_data
        """
        return requests.post('http://reaper:8001', json={self.word: self.link})


class MasterGetWord(Resource):

    def __init__(self, word):
        self.word = word

    def get(self):
        """
        Get data from db by chosen/introduced word in html form
        on localhost:8000/search. Get data from function get_data
        """
        return requests.get(f"http://keeper:8002/{self.word}")


@app.route('/', methods=['GET', 'POST'])
def send_data():
    """
    Get data from html form with word and link
    and call method post from class Master to send data to reaper.
    Redirect on main page anyway, check does data is sending on localhost:8002
    """
    if request.method == 'POST':
        wordDetails = request.form
        word = wordDetails['word']
        link = wordDetails['link']
        Master(word, link).post()
        return redirect('http://localhost:8000')

    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def get_data():
    """
    Get data from html form with word and call method
    post from class MasterGetWord to send request to database
    """
    if request.method == 'POST':
        wordDetails = request.form
        word = wordDetails['word']
        MasterGetWord(word).get()
        return redirect(f"http://localhost:8002/{word}")

    return render_template('search.html')


api.add_resource(Master, '/')
api.add_resource(MasterGetWord, '/search')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
