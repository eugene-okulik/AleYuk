magic_number = 7
print("Попробуйте угадать загаданную цифру:")
while True:
    input_number = int(input())
    if input_number == magic_number:
        print("Поздравляю! Вы угадали!")
        break
    print("Попробуйте снова:")
