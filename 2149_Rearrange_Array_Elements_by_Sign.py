'''
nums = [3,1,-2,-5,2,-4]

pos = [x for x in nums if x > 0]
neg = [x for x in nums if x < 0]

result = []

for i,j in zip(pos, neg):
    result.append(i)
    result.append(j)
    
print(result)

'''

nums = [3,1,-2,-5,2,-4]
n = len(nums)
res = [0] * n

posindex = 0
negindex = 1

for num in nums:
    if num > 0:
        res[posindex] = num
        posindex = posindex + 2
    else:
        res[negindex] = num
        negindex = negindex + 2
        
print (res)
        