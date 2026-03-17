'''
nums = [2,7,11,15]
target = 18 

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Target found")
            print (i,j)

'''    

nums = [2,7,11,15]
target = 9 
hashmap = {}
    
for i, num in enumerate(nums):
    complement = target - num
        
    if complement in hashmap:
        print ( [hashmap[complement], i] )
        
    hashmap[num] = i

        
    