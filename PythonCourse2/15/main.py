# import datetime
# now = datetime.datetime.now()
# print(now)
# from datetime import date
# today = date.today()
# print(today)
# print(today.day)
# print(today.month)
# print(today.year)
# print(today.weekday())
import datetime
now = datetime.datetime.now()
# print("Date :",now)
print("Date Is :",now.strftime("%Y,%m,%d,%A,%I,%M"))
