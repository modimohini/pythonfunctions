"""Given a range of the first 10 numbers, Iterate from the start number to the end number, 
and In each iteration print the sum of the current number and previous number """
previous_number = 0
for x in range(0,10):
    current_number = x   
    sum = current_number + previous_number
    print("current number " + format(x) +" Sum: " + format(sum))
    previous_number = x 

# User Input num 
def sumIteration(userInput):
    previous_number = 0
    for i in range(userInput):
        sum = i + previous_number
        print(format(i) + " Sum:"  + format(sum))
        previous_number = i

in_put = int(input("user num: "))
sumIteration(in_put)
        
