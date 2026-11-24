import os
from datetime import datetime, timedelta

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(data_file_path, 'r') as data_file:
        yield from data_file


for data_line in read_file():
    data = data_line.split(" ")[1:3]
    need_data = " ".join(data)
    need_data_formatted = datetime.strptime(need_data, "%Y-%m-%d %H:%M:%S.%f")
    if data_line[0] == "1":
        print(need_data_formatted + timedelta(weeks=1))
    elif data_line[0] == "2":
        print(need_data_formatted.strftime("%A"))
    elif data_line[0] == "3":
        print((datetime.now() - need_data_formatted).days)
    else:
        print("Не обработано")
