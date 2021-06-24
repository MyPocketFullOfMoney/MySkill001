
def decorator(func):

    def inwarp():
        print('装饰')
        return func()
    return inwarp

@decorator
def print_func():
    print('函数')



print_func()

print(help(iter))