import socket
import time
import threading


def send_client():
    global sock
    while True:
        flag = input("entent: ")
        try:
            sock.send(bytes(flag, encoding="utf-8"))
            print("客户端正在向服务器地址为10.1.32.153，监听端口8001，发送信息 {0}".format(flag))
        except Exception:
            pass

def recv_client():
    global sock
    while True:
        try:
            strSock = sock.recv(1024)
            strSock = bytes.decode(strSock)
            if len(strSock) == 0:
                print("断开")
            else:
                print("收到数据  " + strSock)
            time.sleep(0.1)
        except Exception:
            pass


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(('127.0.0.1', 8001))
sock.connect(('47.98.233.255', 8001))

th1 = threading.Thread(target=send_client, args=(), name="asd")
th2 = threading.Thread(target=recv_client, args=(), name="asd")

th1.start()
th2.start()

th1.join()
th2.join()
sock.close()
