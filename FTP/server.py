# import libreries
import os
import socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

ip = socket.gethostbyname(socket.gethostname())
# create a path for FTP and give the correct location in path
path = 'E:\\FTP'
os.chdir(path)
address = (ip, 21)
authorizer = DummyAuthorizer()
# authorizer.add_user('username', 'password', '.', perm='elradfmw')  
authorizer.add_user('admin', 'admin_password', '.', perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(address, handler)
server.serve_forever()
