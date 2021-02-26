from flask import Flask, jsonify
from flask_restful import Api, Resource, request
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
        """
        Parser that search data on by class. Get dict with {word: link}.
        Return dict {word: count_words}
        """
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
        """
        Send data in Keeper. Call Parser.
        """
        send_data = request.json
        parser_data = ParserReaper(send_data).page_with_vacancy()
        requests.post('http://keeper:8002', json=parser_data)
        return send_data


api.add_resource(ReaperStart, '/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
