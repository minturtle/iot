#-*- coding:utf-8 -*-
import random
import socket

IP = ''
PORT = 5050
SIZE = 1024
ADDR = (IP, PORT)

def run_socket():
    # 서버 소켓 설정
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(ADDR)  # 주소 바인딩
        server_socket.listen()  # 클라이언트의 요청을 받을 준비

        print("server is running")

        # 무한루프 진입
        while True:
            client_socket, client_addr = server_socket.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
            msg = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
            print("[{}] message : {}".format(client_addr, msg))  # 클라이언트가 보낸 메시지 출력


            x = random.choice(['a', 'b', 'c'])
            client_socket.sendall(x.encode())  # 클라이언트에게 응답

if __name__ == '__main__':
    run_socket()

