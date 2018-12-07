import socket

sk = socket.socket()

sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind(('127.0.0.1',8080))

sk.listen()

conn,addr = sk.accept()

ret = conn.recv(1024)
print('server',ret)

conn.send(b'hello !')

conn.close()

sk.close()