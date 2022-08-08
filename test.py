import varModule
import searchIntinList

country = varModule.country_list[1]
print(country)


num = searchIntinList.my_list[2]
print(num)

import time
from importlib import reload

# load 1st time
import varModule
time.sleep(20)
# reload 
reload(varModule)
time.sleep(20) 

 # reload again  
reload(varModule)
print("This is test file..")