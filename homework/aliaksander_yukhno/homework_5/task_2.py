a = "результат операции: 42"
b = "результат операции: 514"
c = "результат работы программы: 9"
position_a = a.index(":")
int_a = int(a[position_a + 1:])
print(int_a + 10)
position_b = b.index(":")
int_b = int(b[position_b + 1:])
print(int_b + 10)
position_c = c.index(":")
int_c = int(c[position_c + 1:])
print(int_c + 10)
