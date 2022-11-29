import socket
from _thread import *
import json
import time
from datetime import datetime


HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


# 서버로부터 메세지를 받는 메소드
# 스레드로 구동 시켜, 메세지를 보내는 코드와 별개로 작동하도록 처리
def recv_data(client_socket) :
    while True :

        data = client_socket.recv(1024)
        print("recieve : ", json.loads(data.decode("utf-8")))


start_new_thread(recv_data, (client_socket,))
print ('>> Connect Server')


#먼저 D127이름으로 등록한다.
message = json.dumps({"CODE" : 100, "BODY" : "D127"},  ensure_ascii = False)
client_socket.send(message.encode("utf-8"))

time.sleep(2)

while True:

    now = datetime.now()

    #50분이 되면 다음시간에 수업이 있는지 체크
    if(now.minute == 50):
        period = now.hour - 7 # 다음시간의 교시
        message = json.dumps({"CODE": 200, "CLASS": "D127", "PERIOD": period, "DAY_WEEK": "화"}, ensure_ascii=False)
        client_socket.send(message.encode("utf-8"))
        time.sleep(60)



client_socket.close()