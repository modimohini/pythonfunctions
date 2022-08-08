my_list = [1,2,3,4]
num = 14
# In oprator
if num in my_list:
    print(num)
else:
    print('not found')
# Not in oprator
def myNOTfun():
    if num not in my_list:
        print("not here")
    else:
        print("got it")

myNOTfun()

#print(4>>2) # binary shift right opration 

for my_list in reversed(my_list):
    print(my_list)
