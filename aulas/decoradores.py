""" from time import sleep, time

def f():
    sleep(.3)

def g():
    sleep(.5)

t = time()
f()
print('f took:', time() - t)

t = time()
g()
print('g took:', time() - t) """


""" from time import sleep, time

def f():
    sleep(.3)

def g():
    sleep(.5)

def measure(func):
    t = time()
    func()
    print(func.__name__, 'took:', time() - t)

measure(f)
measure(g) """


""" from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)

def measure(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took', time() - t)

measure(f, sleep_time=0.3)
measure(f, 0.2) """


""" from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)

def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
    return wrapper

f = measure(f)      # ponto de decoração
f(0.2)
f(sleep_time=0.3)
print(f.__name__)
 """


def func(arg1, arg2, ...):
    pass
func = decorator(func)

# é equivalente ao seguinte:
@ decorator
def func(arg1, arg2,...):
    pass


def func(arg1, arg2,...):
    pass
func = deco1(deco2(func))

# é equivalente ao seguinte:

@deco1
@deco2
def func(arg1, arg2,...):
    pass


def func(arg1, arg2,...):
    pass
func = deco1(deco2(func))

# é equivalente ao seguinte:

@decoarg(arg_a, arg_b)
def func(arg1, arg2, ...):
    pass



from time import sleep, time
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
    return wrapper

@measure
def f(sleep_time=0.1):
    """Eu sou um bebê. Eu adoro dormir!"""
    sleep(sleep_time)

f(sleep_time=0.3)
print(f.__name__, ':', f.__doc__)


from time import sleep, time
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result
    return wrapper

def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print(f'Resultado muito grande({result}). O máximo permitido é 100.')
        return result
    return wrapper

@measure
@max_result
def cube(n):
  return n ** 3

print(cube(2))
print(cube(5))


from functools import wraps

def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f'Resultado é muito grande ({result}). O máximo permitido é {threshold}.')
            return result
        return wrapper
    return decorator

@max_result(75)
def cube(n):
    return n ** 3

print(cube(5))


@max_result(75)
def cube(n):
    return n ** 3

@max_result(100)
def square(n):
    return n ** 2

@max_result(1000)
def multiply(a, b):
    return a * b