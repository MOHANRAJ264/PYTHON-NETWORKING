import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 60000  # Reserve a port for your service.

s.connect((host, port))
print('Successfully connected to server!!!')
t = ''

while not (t == 'send' or t == 'receive'):
    t = input('Enter mode of transmission send or receive: ').lower()
s.send(t.encode())
file_list = s.recv(4096)
file_list = file_list.decode('utf-8')
file_list = eval(file_list)

if t == 'receive':
    print('Available files')
    for item in file_list:
        print(' ' + item)
    filename = ''
    while filename not in file_list:
        filename = input('Enter filename which shown above :')
    s.send(filename.encode())

    with open(f'received_{filename}', 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            data = s.recv(1024)
            # print('data=%s', data)
            if not data:
                break
            # write data to a file
            f.write(data)
        f.close()
        print('Successfully get the file')

if t == 'send':
    filename = ''
    f = ''
    fb = ''
    while True:
        try:
            filename = input('enter file to send with extension')
            f = open(filename, 'rb')
        except FileNotFoundError:
            print('no such file')
            continue
        except IOError:
            print('oops something went wrong')
            continue
        else:
            # print('success')
            break
    if filename in file_list:
        exist = ''
        print('The filename is already available in the ser  ver')
        while exist not in ["Y", "N"]:
            exist = input("Do you want to replace the existing file ? ( Y or N) ").upper()
        if exist == 'N':
            file_and_extension = filename.split(".")
            count_file_copies = 0
            for file in file_list:
                temp = file.split(".")
                if temp[0][:len(file_and_extension[0]):] == file_and_extension[0]:
                    count_file_copies += 1
            final_name = file_and_extension[0]+'_'+str(count_file_copies)+'.'+file_and_extension[1]
            print(f'Your file is going to be saved in the name {final_name}')
            s.send(final_name.encode())
        if exist == 'Y':
            s.send(filename.encode())
    fb = f.read(1024)
    while fb:
        s.send(fb)
        # print('Sent ', repr(fb))
        fb = f.read(1024)
    f.close()
    print('done sending')
s.close()
print('connection closed')
