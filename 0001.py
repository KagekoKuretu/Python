# Creating 200 random activation codes
# codes are like aaaa-bbbb-cccc-dddd

import string
import random

charset=string.ascii_letters+string.digits
list1 = []

for code_num in range(0,200):
    code = [0,"-",0,"-",0,"-",0]
    for code_sec in range (0,4):
        random_code=''.join(random.sample(charset,4))
        code[code_sec*2] = random_code

    code=''.join(code)
    list1.append(code)    

print("\n".join(list1))
