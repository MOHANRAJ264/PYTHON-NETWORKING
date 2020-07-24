
from socket import *


def server_program():
   
    try:
         # get the hostname
        host = gethostname()
        port = 8000 

        #TCP Continuos data stream
        server_socket = socket(AF_INET,SOCK_STREAM)
        server_socket.bind((host, port)) 

            
        server_socket.listen(2)
        #conn is client_socket
        print("connectinggggg............")
        conn, address = server_socket.accept()# accept new connection
        print("Connection from: " + str(address))
        count=0
        while True:  
            if count==0:
                data = conn.recv(1024).decode()
                data="Hello " + str(data)+", How Can I help you"
                count+=1
                print("server :",data)
                #data=input("server :")
            else:
                #data = conn.recv(1024).decode()
                print("client :",data)
                # receive data stream. it won't accept data packet greater than 1024 bytes
                if data.lower().strip()!='bye':
                    data = input('server : ')
            # if not data:
            #         break
            conn.send(data.encode())
            data = conn.recv(1024).decode()
            if data.lower().strip()=='bye':
                conn.close()  # close the connection
                

        
    except OSError as e:
        # print("alert :")
        # print("OSERROR : {0}".format(e))
        print('Client disconnected')
        print('Waiting for next connection')
            
        


if __name__ == '__main__':
    while True:
        server_program()
