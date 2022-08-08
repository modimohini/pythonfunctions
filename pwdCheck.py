
def pwdcheck(pwd):
    if pwd == "hello":
        print("good")
    else:
        print("try again")

pwdcheck("hello")


print("num in reverse")
num = 5
for num in (range(num,1,-1)):
    print(num)