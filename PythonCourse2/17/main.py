# def Sum(number1,number2):
#     assert (type(number1) is int and type(number2) is int), "Number Must Be Int"
#     return number1 + number2
# print(Sum("3",5))
# try:
#     x = 30
#     if x > 20:
#         raise Exception("Your Number Is Very Big")
# except Exception as err:
#     print("error :", err)
try:
    x = 30
    if x>20:
        print("Number IS Ok")
except Exception as err:
    print(err)
else:
    print("Complete")