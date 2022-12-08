# Write
fileopen = open("hi.txt", "w")
fileopen.write("TopLearn\n")
fileopen.write("GetWork\n")
fileopen.close()
print("Finish")
# ----------------------------------------------------------------------
# Continue
fileopen = open("hi.txt", "a")
fileopen.write("Hi")
fileopen.close()
print("Finish 2")
# ----------------------------------------------------------------------
# Read
fileopen = open("hi.txt", "r")
print(fileopen.read())
fileopen.close()
# ----------------------------------------------------------------------
fileopen = open("hi.txt", "r")
print("\n New Print \n")
print(fileopen.readline())
fileopen.close()
