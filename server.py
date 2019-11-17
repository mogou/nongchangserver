import socket
import mysql.MySQLDB
import threading
import time

conneList = []
sock = None
lastpeopel_num = 0
lock_ = threading.Lock()

def recv_action():
    global conneList
    global lastpeopel_num

    while True:
        lock_.acquire()
        for i in range(len(conneList)):
            # client_socket.settimeout(10)
            #print("111----: " + str(conneList[i][1]))
            try:
                buf = conneList[i][0].recv(1024)
                buf = bytes.decode(buf)
                print(str(conneList[i][1]) + "  get value  " + buf)

                if buf is not None or len(buf) != 0:
                    for j in range(len(conneList)):
                        #print("2222----: " + str(conneList[j][1]))
                        strvalue = "0002" + str(conneList[j][1]) + buf
                        try:
                            conneList[j][0].send(bytes(strvalue, encoding="utf-8"))
                        except ConnectionResetError:
                            conneList.remove(conneList[j])
                            lastpeopel_num = 0
                            pass
                else:
                    conneList.remove(conneList[i])
                    lastpeopel_num = 0
                    print("out")

            except ConnectionAbortedError:
                print("ConnectionAbortedError  player QZ exit")
                print("remove player " + str(conneList[i][1]))
                conneList.remove(conneList[i])
                lastpeopel_num = 0
                pass
            except ConnectionResetError:
                print("ConnectionResetError  player QZ exit")
                print("remove player " + str(conneList[i][1]))
                conneList.remove(conneList[i])
                lastpeopel_num = 0
                pass
            except socket.timeout:
                print("remove player " + str(conneList[i][1]))
                conneList.remove(conneList[i])
                lastpeopel_num = 0
                pass
            except Exception:
                pass
        lock_.release()
        time.sleep(0.1)


def send_action():
    global lastpeopel_num
    global conneList

    while True:
       
        lock_.acquire()
        if lastpeopel_num != len(conneList) and len(conneList) != 0:
            lastpeopel_num = len(conneList)
            for client_socket, client_addr in conneList:
                try:
                    str_value = "0001" + str(len(conneList))
                    client_socket.send(bytes(str_value, encoding="utf-8"))
                except ConnectionAbortedError:
                    print("ConnectionAbortedError  player QZ exit")
                    conneList.remove((client_socket, client_addr))
                    print("remove player " + str(client_addr))
                    lastpeopel_num = 0
                    pass
                except ConnectionResetError:
                    print("ConnectionResetError  player QZ exit")
                    conneList.remove((client_socket, client_addr))
                    print("remove player " + str(client_addr))
                    lastpeopel_num = 0
                    pass
                except Exception:
                    pass
        lock_.release()
        time.sleep(0.1)


def accept_action():
    global conneList
    global sock

    while True:
        try:
            connection, address = sock.accept()
            lock_.acquire()
            conneList.append((connection, address))
            connection.setblocking(False)
            lock_.release()
            print(str(address) + "server lin num is " + str(len(conneList)))
        except Exception:
            pass
        time.sleep(0.1)

def listen_socket():
    global conneList
    global sock
    global lastpeopel_num
    s = mysql.MySQLDB.DD()
    s.get_connect()
    lastpeopel_num = 0

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 8001))
    # sock.bind(('47.98.233.255', 8001))
    sock.listen(5)
    sock.setblocking(False)
    print("server Start Server_addr is 47.98.233.255 listen 8001 max link 5")

    th_accept = threading.Thread(target=accept_action, args=(), name="accept_thread")
    th_recv = threading.Thread(target=recv_action, args=(), name="recv_thread")
    th_send = threading.Thread(target=send_action, args=(), name="send_thread")
    th_accept.start()
    th_recv.start()
    th_send.start()

    th_accept.join()
    th_recv.join()
    th_send.join()
    sock.close()





