import random

print("Какую зарплату ожидаете?")
salary = int(input())
bonus = random.choice([True, False])
if bonus:
    result = salary + random.randrange(1, 10001)
else:
    result = salary
print(result)
