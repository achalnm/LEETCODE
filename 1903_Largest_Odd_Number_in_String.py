num = "35427"
        
for i in range(len(num) - 1, -1, -1):
    if int(num[i]) % 2 != 0:  
        print(num[:i + 1])
        break    
print("")  

'''
nums = "42036"
maxis_index = -1
for i in range(len(nums)-1, -1, -1):
    if int(nums[i]) % 2 != 0:
        maxis_index = i
        break  

if maxis_index != -1:
    print(nums[:maxis_index+1])
else:
    print("no odd number in the string")
'''   
'''
nums = "43046"
number = []
num_digits = len(nums)

intnums = int(nums)

for i in range(num_digits):
    digit = intnums % 10
    intnums = intnums // 10
    if (digit % 2 == 0):
        number.append(digit)
    else:
        break

numbers = str(number)
print (numbers)
'''

    
