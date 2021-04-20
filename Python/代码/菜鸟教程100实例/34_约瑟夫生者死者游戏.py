# 约瑟夫生者死者游戏
# 时间：2020/12/28
"""
30 个人在一条船上，超载，需要 15 人下船。
于是人们排成一队，排队的位置即为他们的编号。
报数，从 1 开始，数到 9 的人下船。
如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？

"""

# 创建代表人数的空字典
people = {}
print(type(people))

# 
for x in range(1,31):
    people[x] = 1
print(people)
check = 0
move_flag = 1
stop_falg = 0
while move_flag <= 31:
    # 报数在31后，重新开始
    if move_flag == 31:
        move_flag = 1
    # 15个人下船，退出循环
    elif stop_falg == 15:
        break
    # 已经下船的人，不再加入循环,跳过，进行下一次循环
    else:
        if people[move_flag] == 0:
            move_flag += 1
            continue
        else:
            check += 1
            # 报数到第9人，下船
            if check == 9 :
                # 下船,标志置0
                people[move_flag] = 0
                # 检查位重新置0
                check = 0
                print("{0}号下船".format(move_flag))
                # 下船人数+1
                stop_falg += 1
            # 否则继续循环
            else:
                move_flag += 1
# 循环结束，再输出一遍字典
print("游戏结束!",people)

