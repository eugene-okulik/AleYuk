def repeat_me(count):
    def func_dec(func):
        def wrapper(*args):
            res = None
            for _ in range(count):
                res = func(*args)
            return res
        return wrapper
    return func_dec


@repeat_me(count=2)
def repeated_text(text):
    print(text)


repeated_text('print me')