import datetime


example = "Jan 15, 2023 - 12:05:33"
datetime_date = datetime.datetime.strptime(example, "%b %d, %Y - %H:%M:%S")
print(datetime_date.strftime("%B"))
print(datetime_date.strftime("%d.%m.%Y, %H:%M"))
