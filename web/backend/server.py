from flask import Flask, request
from flask_cors import CORS
import socket
from _thread import *
import json
import time


HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():

    classroom = request.args["classroom"]
    dayweek = request.args["dayweek"]
    period = request.args["period"]

    message = json.dumps({"CODE": 20, "CLASS": classroom, "PERIOD": period, "DAY_WEEK": dayweek}, ensure_ascii=False)
    print(message)
    client_socket.send(message.encode("utf-8"))
    data = client_socket.recv(1024)
    return data

if __name__ =="__main__" :
    app.run('0.0.0.0', port=5000, debug=True)