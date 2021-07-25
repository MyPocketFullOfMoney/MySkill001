import threading

def write_string(string, path="test.csv"):
    with open(path, 'a') as f:
        f.write(string + "\r\n")

# 创建新线程
for i in range(15):
	# 这里每次循环都开一个线程，并写入"写入:" + i，args里指定参数，注意要使用list[]格式
    thread1 = threading.Thread(target=write_string, args=("写入_1: " + str(i),))
    thread1.start()
