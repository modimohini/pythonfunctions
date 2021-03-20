words = ["foo", "buzz", "bar"]
userInput = input("please enter your word: ")

if userInput in words:
    print("true")
elif userInput == '*':
    print("true")
elif userInput == "":
    print("not valid input")
else:
    print("false")
