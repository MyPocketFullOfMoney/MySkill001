# Python文件基础操作，包括open,read,write
# 时间:2020/10/18

# 写文件
with open('test.txt','wt',encoding = 'utf8') as out_file:
    out_file.write("Python程序写入：123——test")

# Read a file
with open('test.txt','rt',encoding='utf8') as in_file:
    text = in_file.read()
print(text)