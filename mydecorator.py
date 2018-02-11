import functools
#decorator就是一个返回函数的高阶函数，要定义一个能打印日志的decorator
def log(arg='call'):    #默认参数
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (arg, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print("2017-8-19")

@log()
def now2():
    print("2017-8-19")

now()
now2()

int2 = functools.partial(int,base=2)    #偏函数（通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点）
print (int2('11101'))

my_max = functools.partial(max,10)  #10会被自动加到最左边
print (my_max(2,8,6,0))