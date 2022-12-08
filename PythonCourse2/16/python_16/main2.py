# ----------------------------------------------------------------------
import os
# os.rename("hi.txt", "toplearn.txt")
# os.remove("toplearn.txt")
# os.mkdir("files")
# os.removedirs("files")
# fileopen = open("hi.txt", "w")
# fileopen.write("hi")
# fileopen.close()
if not os.path.exists("files"):
    os.mkdir("files")
    print("created!")

else:
    print("Exist")
