from flask import Flask, render_template, url_for, redirect, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
api = Api(app)

db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)


class Keeper(Resource):

    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM words')
        row_headers = [x[0] for x in cur.description]
        rv = cur.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return jsonify(json_data)

    def post(self):
        send_data = request.json
        cur = mysql.connection.cursor()
        print(send_data)
        for i in send_data:
            cur.execute("INSERT INTO words(word, count_words) VALUES(%s, %s)", (i, send_data[i]))
            mysql.connection.commit()
        cur.close()
        return 'success'


class KeeperItems(Resource):

    def get(self, search_word):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM words WHERE word = %s", [search_word])
        row_headers = [x[0] for x in cur.description]
        rv = cur.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return jsonify(json_data)


api.add_resource(Keeper, '/')
api.add_resource(KeeperItems, '/<search_word>')
if __name__ == '__main__':
    app.run(host='127.0.0.3', port=5000, debug=True)
