temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
hi_temp_list = list(filter(lambda temp: temp > 28, temperatures))
print(max(hi_temp_list))
print(min(hi_temp_list))
print(sum(hi_temp_list) / len(hi_temp_list))
