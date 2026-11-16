def add_finish(func):

    def wrapper(*args):
        func(*args)
        print("finished")

    return wrapper


@add_finish
def print_text(text):
    print(text)


print_text('print me')
