import time

from flask import Flask, request
from flask_cors import CORS
import socket
import json



HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = json.dumps({"CODE": 10, "BODY": "WEB"}, ensure_ascii=False)
client_socket.send(message.encode("utf-8"))
client_socket.recv(1024)

app = Flask(__name__)
CORS(app)


@app.route("/class/time")
def getClassTime():

    classroom = request.args["classroom"]
    dayweek = request.args["dayweek"]
    period = request.args["period"]

    message = json.dumps({"CODE": 20, "CLASS": classroom, "PERIOD": period, "DAY_WEEK": dayweek}, ensure_ascii=False)
    client_socket.send(message.encode("utf-8"))
    data = client_socket.recv(1024)

    return data

@app.route("/class/attendance")
def getClassAttendance():

    classroom = request.args["classroom"]
    message = json.dumps({"CODE": 30, "CLASS": classroom}, ensure_ascii=False)
    client_socket.send(message.encode("utf-8"))
    data = client_socket.recv(1024)

    return data

if __name__ =="__main__" :
    app.run('0.0.0.0', port=5000, debug=True)