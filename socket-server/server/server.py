import socket
from _thread import *
import json
import db

clients = {} # 서버에 접속한 클라이언트 목록

# 서버 IP 및 열어줄 포트
HOST = '127.0.0.1'
PORT = 9999

def main():
    # 서버 소켓 생성
    print('>> Server Start')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    try:
        while True:
            print('>> Wait')

            client_socket, addr = server_socket.accept()
            start_new_thread(threaded, (client_socket, addr))

    except Exception as e:
        print('error : ', e)

    finally:
        server_socket.close()


# 쓰레드에서 실행되는 코드입니다.
# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다.
def threaded(client_socket, addr):
    print('>> Connected by :', addr[0], ':', addr[1])

    # 클라이언트가 접속을 끊을 때 까지 반복합니다.
    while True:

        try:
            # 클라이언트의 요청을 대기합니다.
            raw_data = client_socket.recv(1024)
            if not raw_data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

            data = json.loads(raw_data.decode("utf-8"))
            print(data)
            if data == None : continue

            #서버에서 request 분석 후 알맞은 응답 정보 생성
            resp = parse_data(data, client_socket)
            if(resp == None): continue
            client_socket.send(json.dumps(resp, ensure_ascii = False).encode('utf-8'))

        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

    if client_socket in clients :
        clients.remove(client_socket)
        print('remove client list : ', len(clients))

    client_socket.close()



''''
CODE 1X : BODY의 이름으로 클라이언트 추가
CODE 2X : CLASS, PERIOD, DAY_WEEK 값으로 해당 교실의 수업여부 조회
CODE 3X : CLASS 값으로 해당 교실의 출석 인원 수를 분석해서 조회
CODE 4X : 라즈베리로부터 출석 인원수를 받음.
CODE 5X : CLASS 값으로 해당 교실의 온도를 측정해서 조회
CODE 6X : 라즈베리베리로부터 온습도를 받음.
CODE 7X : CLASS, HOPE_TEMPERATURE 값으로 해당 교실의 온도를 조정
응답 코드:
CODE X1 : 정상적인 응답
CODE X2 : 데이터 부재
CODE X3 : 서버 오류
'''
def parse_data(data, client_socket):
    if data['CODE'] == 10:
        clients[data['BODY']] = client_socket
        return {"CODE" : 11, "BODY" : "OK"}

    elif data['CODE'] == 20:
        # 해당 요일, 시간, 강의실의 수업정보
        result = db.get_class_data(data["CLASS"], data["PERIOD"], data["DAY_WEEK"])
        if len(result) == 0: return {"CODE" : 22}
        else: return {"CODE" : 21, "BODY" : result[0]}

    elif data['CODE'] == 30:
        if not data['CLASS'] in clients : return {"CODE" : 33}

        # 해당 강의실과 연결된 라즈베리파이로 갯수를 요청한다.
        clients[data['CLASS']].send(json.dumps({"CODE" : 30}).encode('utf-8'))

        return None
    elif data['CODE'] == 40:
        clients["WEB"].send(json.dumps(data, ensure_ascii=False).encode('utf-8'))

    elif data['CODE'] == 50:
        if not data['CLASS'] in clients: return {"CODE": 53}

        # 해당 강의실과 연결된 라즈베리파이로 갯수를 요청한다.
        clients[data['CLASS']].send(json.dumps({"CODE": 50}).encode('utf-8'))

    elif data['CODE'] == 60:
        clients["WEB"].send(json.dumps(data, ensure_ascii=False).encode('utf-8'))

    elif data['CODE'] == 70:
        if not data['CLASS'] in clients: return {"CODE": 73}
        clients[data['CLASS']].send(json.dumps(data).encode('utf-8'))

        return {"CODE" : 71}
if __name__=="__main__":
    main()