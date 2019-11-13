import socket
import mysql.MySQLDB

def listen_socket():

    s = mysql.MySQLDB.DD()
    s.get_connect()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8001))
    # sock.bind(('47.98.233.255', 8001))
    sock.listen(5)
    sock.setblocking(False)
    print("server Start,Server_addr is 47.98.233.255,listen 8001,max link 5")

    conneList = []
    while True:
        try:
            # print("wati link ....")
            connection, address = sock.accept()
            conneList.append((connection, address))
            print("server lin num is : " + str(len(conneList)))
        except BlockingIOError:
            pass

        for client_socket, client_addr in conneList:
            # client_socket.settimeout(10)
            try:
                buf = client_socket.recv(1024)
                buf = bytes.decode(buf)
                print(str(client_addr) + "  get value:  " + buf)

                if buf is not None:
                    for client_, addr_ in conneList:
                        strvalue = str(client_addr) + buf
                        try:
                            client_.send(bytes(strvalue, encoding="utf-8"))
                        except ConnectionResetError:
                            conneList.remove((client_, addr_))
                else:
                    print("out")

            except ConnectionResetError:
                print("player QZ exit")
                conneList.remove((client_socket, client_addr))
                print("remove player: " + str(client_addr))
                pass
            except socket.timeout:
                conneList.remove((client_socket, client_addr))
                print("remove player: " + str(client_addr))
            except BlockingIOError:
                pass

