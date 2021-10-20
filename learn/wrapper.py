import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("start call %s():" % func.__name__)
        func(*args, **kw)
        print("end call %s():" % func.__name__)

    return wrapper


@log
def now():
    print("2021-10-20")


now()


def loginfo(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@loginfo("execute")
def nowinfo():
    print("2021-10-20")


nowinfo()
