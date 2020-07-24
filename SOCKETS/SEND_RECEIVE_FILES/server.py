import socket  # Import socket module
import os      # Import os module

port = 60000  # Reserve a port for your service.
s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
s.bind((host, port))  # Bind to the port
s.listen(5)  # Now wait for client connection.

print(f'Server listening on port {port}....')

# This while loop make the server runs forever
while True:
    try:
        conn, address = s.accept()  # Establish connection with client.
        print('Got connection from', address)
        operation = conn.recv(1024)  # Get operation mode from client
        operation = operation.decode()

        file_list = []  # File list in server
        for subdir, dirs, files in os.walk('./'):
            for file in files:
                file_list.append(file)
        final_list = str(file_list)
        conn.send(final_list.encode())
        if operation == 'receive':
            filename = conn.recv(1024)
            filename = filename.decode()
            print(filename)
            f = open(filename, 'rb')
            fb = f.read(1024)
            while fb:
                conn.send(fb)
                # print('Sent ', repr(fb))
                fb = f.read(1024)
            f.close()
            print('Done sending')

        elif operation == 'send':
            filename = conn.recv(1024)
            filename = filename.decode()
            with open(filename, 'wb') as f:
                print('File opened')
                while True:
                    print('receiving data...')
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)  # write data to a file
                f.close()
                print('File received')

        print('Connection closed for :', address)
        conn.close()
    except ConnectionResetError:
        print('Client disconnected')
        print('Waiting for next connection')
        continue
