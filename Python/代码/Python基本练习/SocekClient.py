import socket

# 创建一个socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立连接
client_socket.connect(('127.0.0.1',10086))

# 接收欢迎消息
print(client_socket.recv(1024).decode('utf-8'))

for client_data in [b'DD',b'AA',b'CCC']:
    # 发送数据
    client_socket.send(client_data)
    # 打印返回的消息
    print(client_socket.recv(1024).decode('utf-8'))

client_socket.send(b'exit')
# 关闭连接
client_socket.close()
