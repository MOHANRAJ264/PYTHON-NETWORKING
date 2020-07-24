

import socket

def client_program():
    try:
        host = socket.gethostname()  # as both code is running on same pc
        port = 8000  # socket server port number

        client_socket = socket.socket()  
        client_socket.connect((host, port))  # connect to the server

        message="waiting_for_user_name"

        while message.lower().strip() != 'bye':
            #client_socket.send(message.encode())  # send message
            #data = client_socket.recv(1024).decode()  # receive response
            if message=="waiting_for_user_name":
                message = input("Enter Youe name -> ")
            
            else:
                print('server : ' + str(data))  

                message = input("client : ")
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()

        client_socket.close()
    except ConnectionRefusedError as e:
        print("ConnectionRefusedError: {0}".format(e))
    finally:
        client_socket.close()
if __name__ == '__main__':
    client_program()
