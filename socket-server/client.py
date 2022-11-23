import socket

# 접속 정보 설정
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5050
SIZE = 1024
SERVER_ADDR = (SERVER_IP, SERVER_PORT)


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(SERVER_ADDR)  # 서버에 접속
        s = input("보낼 매시지를 입력해주세요")
        client_socket.send(s.encode())  # 서버에 메시지 전송
        msg = client_socket.recv(SIZE)  # 서버로부터 응답받은 메시지 반환
        print("resp from server : {}".format(msg))  # 서버로부터 응답받은 메시지 출력


if __name__ == '__main__':
    run_client()