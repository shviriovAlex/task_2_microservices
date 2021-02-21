from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource, request
import re
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
api = Api(app)


class ParserReaper:

    def __init__(self, words_links):
        self.headers = {'user-agent': 'my-app/0.0.1'}
        self.all_words = {}
        self.words_links = words_links

    def page_with_vacancy(self):
        for cv_page in self.words_links:
            cv_page_soup = BeautifulSoup(requests.get(self.words_links[cv_page], headers=self.headers).content,
                                         'html.parser').find_all(
                class_="vacancy-serp")
            for word in self.words_links:
                if word not in self.all_words:
                    self.all_words.setdefault(word,
                                              [len(re.findall(word, str(cv_page_soup).lower()))])
                else:
                    self.all_words[word].append(len(re.findall(word, str(cv_page_soup).lower())))

        return self.all_words


class ReaperStart(Resource):

    def post(self):
        send_data = request.json
        parser_data = ParserReaper(send_data).page_with_vacancy()
        requests.post('http://127.0.0.3:5000', json=parser_data)
        return jsonify(send_data)


api.add_resource(ReaperStart, '/')
if __name__ == '__main__':
    app.run(host='127.0.0.2', port=5000, debug=True)