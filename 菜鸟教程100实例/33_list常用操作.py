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
print("="*40,"list删除元素","="*40)
print("list =",li)
li.remove("z")
print("删除元素z,list =",li)
# pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
print("删除列表最后一个元素：",li.pop())
print(li)
print("="*40,"list删除元素","="*40)