import socket
import threading
import time


def tcplink(sock,addr):
    print('Accept a new connection from {}'.format(addr))
    sock.send(b'Welcome!')
    # 接收客户端数据
    while True:
        server_data = sock.recv(1024)
        time.sleep(1)
        if not server_data or server_data.decode('utf-8') == 'exit':
            break
        #sock.send((b'Hello! This is SERVER,you data is that ',server_data.decode('utf-8')).encode('utf-8'))
        sock.send(('Hello, %s!' % server_data.decode('utf-8')).encode('utf-8'))
        
    sock.close()
    print('Connection from {} colsed'.format(addr))





# 创建一个socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定端口
server_socket.bind(('127.0.0.1',10086))
# 开始监听
server_socket.listen(5)
print('Wating for connection ...')

while True:
    # 接收一个新连接
    sock,addr = server_socket.accept()
    # 创建一个新线程处理连接
    solution_t = threading.Thread(target=tcplink,args=(sock,addr))
    solution_t.start()



