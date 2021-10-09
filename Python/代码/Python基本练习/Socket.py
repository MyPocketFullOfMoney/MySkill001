import socket

# 创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 创建TCP连接
# 参数类型为元组，('地址',端口号)
s.connect(('www.baidu.com',80))


# 发送数据，数据是一个HTTP请求
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []

while True:
    # 每次最多接收字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

# 关闭连接
s.close()

# 将HTTP头部和网页内容分离
header,html = data.split(b'\r\n\r\n',1)

print(header.decode('utf-8'))

# html内容写入文件
with open('sina.html','wb') as f:
    f.write(html)