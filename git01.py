print("Hi, What's your name?")
name=input("My name is ")
print(f"{name}, which do you want to do, reading or sleeping?")
do=input("reading/sleeping")
if do=="reading":
    print("OK, let's read together!")
    print("What will we read?")
    book=input("book name : ")
else:
    print("OK, let's sleeping together")
    print("What about play a song?")
    a1=input("Y/N")