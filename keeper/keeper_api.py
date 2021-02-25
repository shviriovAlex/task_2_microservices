from flask import Flask, render_template, redirect, jsonify
from flask_restful import Api, Resource, request, reqparse
import mysql.connector
import json

app = Flask(__name__)
api = Api(app)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'task_docker'
}


class Keeper(Resource):

    def get(self):
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM words')
        results = [word[0] for word in cursor.description]
        all_rows = cursor.fetchall()
        json_data = []
        for word in all_rows:
            json_data.append(dict(zip(results, word)))
        return jsonify(json_data)


    def post(self):
        send_data = request.get_json()
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        print(send_data)
        for i in send_data:
            cursor.execute("INSERT INTO words(word, count_words) VALUES(%s, %s)", (i, send_data[i][0]))
            connection.commit()
        cursor.close()
        connection.close()
        return 'success'


class KeeperItems(Resource):

    def get(self, search_word):
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM words WHERE word = %s", [search_word])
        results = [word[0] for word in cursor.description]
        all_rows = cursor.fetchall()
        json_data = []
        for word in all_rows:
            json_data.append(dict(zip(results, word)))
        return jsonify(json_data)


api.add_resource(Keeper, '/')
api.add_resource(KeeperItems, '/<search_word>')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002, debug=True)
