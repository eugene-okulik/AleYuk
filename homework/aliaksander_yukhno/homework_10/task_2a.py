def repeat_me(func):

    def wrapper(*args, count):
        res = None
        for _ in range(count):
            res = func(*args)
        return res
    return wrapper


@repeat_me
def repeated_text(text):
    print(text)


repeated_text('print me', count=2)
