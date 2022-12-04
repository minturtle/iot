import socket
from _thread import *
import json
import time
from datetime import datetime
from image_service import get_person_count

HOST = '34.168.65.229'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def parse_data(data):
    if(data["CODE"] == 30):
        person_count = get_person_count("images/img.jpg")
        return {"CODE" : 40, "COUNT" : person_count}
    if(data["CODE"] == 50):
        return {"CODE" : 60, "temperature" : 23 , "humid" : "30%"}
    if (data["CODE"] == 70):
        print("set temperature : " + data["HOPE_TEMPERATURE"])
        return {"CODE" : 71}

# 서버로부터 메세지를 받는 메소드
# 스레드로 구동 시켜, 메세지를 보내는 코드와 별개로 작동하도록 처리
def recv_data(client_socket) :
    while True :
        data = client_socket.recv(1024)
        json_data = json.loads(data.decode("utf-8"))

        result = parse_data(json_data)
        message = json.dumps(result, ensure_ascii = False)
        client_socket.send(message.encode("utf-8"))


start_new_thread(recv_data, (client_socket,))
print ('>> Connect Server')


#먼저 D127이름으로 등록한다.
message = json.dumps({"CODE" : 10, "BODY" : "D127"}, ensure_ascii = False)
client_socket.send(message.encode("utf-8"))

time.sleep(2)

while True:
    days = ["월", "화", "수", "목", "금", "토", "일"]

    now = datetime.now()
    week_idx = datetime.today().weekday()

    #50분이 되면 다음시간에 수업이 있는지 체크
    if(now.minute == 50):
        period = now.hour - 7 # 다음시간의 교시
        message = json.dumps({"CODE": 20, "CLASS": "D127", "PERIOD": period, "DAY_WEEK": days[week_idx]}, ensure_ascii=False)
        client_socket.send(message.encode("utf-8"))
        time.sleep(60)



client_socket.close()