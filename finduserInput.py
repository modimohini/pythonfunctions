

def matchword():
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

# matchword()

def match(x):
    word = ["hi","hello", "hola"]
    if x in word:
        print("true")
    else:
        print("false")

match("h")


