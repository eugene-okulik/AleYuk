import sys
sys.set_int_max_str_digits(0)


def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def numb_in_fibo(n):
    i = 1
    for numb in fibo():
        if i == n:
            print(numb)
            break
        i += 1


numb_in_fibo(5)
numb_in_fibo(200)
numb_in_fibo(1000)
numb_in_fibo(100000)
