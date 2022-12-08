# Refrences
import Password.CreatePassword as MyPassword
while True:
    userPasswordLength = int(input("Enter Your Password Length : \n"))
    print(MyPassword.GeneratePassword(userPasswordLength))
    reply = input("Do You Want To Try Again?(y,n)")
    if reply.lower() == "y":
        continue
    elif reply.lower() == "n":
        break
