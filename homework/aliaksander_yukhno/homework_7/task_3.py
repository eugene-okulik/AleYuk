a = "результат операции: 42"
b = "результат операции: 54"
c = "результат работы программы: 209"
d = "результат: 2"


def new_sum(numb):
    return int(numb.split(":")[1]) + 10


print(new_sum(a))
print(new_sum(b))
print(new_sum(c))
print(new_sum(d))
