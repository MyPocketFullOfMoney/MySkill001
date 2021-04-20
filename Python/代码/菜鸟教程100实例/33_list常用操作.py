# list的常用操作
# 时间：2020/12/14

# 1、list定义
li = ["a" , "b" , "mpilgrim" , "z" , "example"]
print("定义的列表：list = ",li)

# 2、list负数索引
print("负数索引，从后往前检索，-1代表最后一位元素！")
print("list[-1] = ",li[-1])
print("list[-3] = ",li[-3])
print("切片为左闭右开，下标从0开始")
print("list[1:3] = ",li[1:3])
print("list[1:-1] = ",li[1:-1])
print("list[0:3] = ",li[0:3])

# 3、list增加元素
li.append("new")
print("列表新增元素\"new\",list=",li)
li.insert(2,"new_1")
print("列表在下标2中插入元素new_1,list=",li)
# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
li.extend(["two","elements"])
print(li)

# 4、list搜索
# index() 函数用于从列表中找出某个值第一个匹配项的索引位置
print("="*40,"list搜索","="*40)
print("单词example的下标：",li.index("example"))
print("new的下标：",li.index("new"))
print("判断字母c是否存在列表","c" in li)
print("="*40,"list搜索","="*40)

# 5、list删除元素
print("="*40,"5、list删除元素","="*40)
print("list =",li)
li.remove("z")
print("删除元素z,list =",li)
# pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
print("删除列表最后一个元素：",li.pop())
print(li)
print("="*40,"list删除元素","="*40)

# 6、list运算符
print('\n')
print("="*40,"6、list运算符","="*40)
list_6 = ['a','b','mpilgrim']
print('list_6 + [\'example\',\'new\'] =',list_6 + ['example','new'])
print("="*40,"list运算符","="*40)

# 7、使用join链接list成为字符串
print("="*40,"7、join链接list成为字符串","="*40)
print('穿插个字典操作')
params = {"server":"mpilgrim","database":"master","uid":"sa","pwd":"secret"}
print(f'字典params={params}')
dict_list = [(k,v) for k,v in params.items()]
print(dict_list)
print(";".join(["{0}={1}" .format(k, v) for k, v in params.items()]))

# 8、list分割字符串
print("="*40,"8、list分割字符串","="*40)
list_8 = ['server=mpilgrim','uid=sa','database=master','pwd=secret']
str_8 = ";".join(list_8)
print('连接成字符串：',str_8)
# 通过split函数拆分
print('拆分后：',str_8.split(";"))
# split函数可以接受第二个参数，表示要拆分的次数
print('拆分一次:',str_8.split(";",1))

# 9、list的映射解析
print("="*40,"9、list的映射解析","="*40)
list_9 = [1,9,8,4]
result_9 = [elem*2 for elem in list_9]
print(result_9)

# 10、dictionary中的解析
print("="*40,"10、dictionary中的解析","="*40)
params_10 = params
print('字典params的key:',params_10.keys())
print('字典params的value:',params_10.values())
# 通过items函数获取字典的key:value
print('items函数获取key:',[k for k , v in params_10.items()])
print('items函数获取value:',[v for k , v in params_10.items()])
print('items函数获取key:value',['{0}={1}'.format(k,v) for k,v in params_10.items()])

# 11、list过滤
print("="*40,"11、list过滤","="*40)
list_11 = ["a","mpilgrim","foo","b","c","b","d","d"]
# 过滤长度小于等于1的元素
result_11 = [elem for elem in list_11 if len(elem) > 1]
print('长度大于1的元素：',result_11)
# 过滤重复的元素
result_12 = [elem for elem in list_11 if list_11.count(elem) == 1]
print('过滤重复的元素',result_12)