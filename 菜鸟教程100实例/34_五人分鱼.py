# 五人分鱼
"""
A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。

B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。

C、D、E依次醒来，也按同样的方法拿鱼。

问他们至少捕了多少条鱼?
"""

def Fish():
    # 设置鱼的初始值
    fish = 1
    while True:
        total,enough = fish,True
        # 循环5次，每次按相同规则分鱼
        for _ in range(5):
            if (total - 1) % 5 == 0:
                # 更新每次分鱼前鱼的总数
                total = (total - 1) // 5 * 4
            # 如果不能满足，则退出分鱼的循环
            else:
                enough = False
                break
        # 判断是否满足5次分鱼，不满足则继续
        if enough:
            print('总共有{}条鱼'.format(fish))
            break
        fish += 1

if __name__ == '__main__':
    Fish()