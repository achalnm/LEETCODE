nums = [int(x) for x in input("Enter the array: ").split()]

candidate = None
count = 0

for num in nums:
    if count == 0:
        candidate = num
    count = count + (1 if num == candidate else -1)

print("Majority element is:", candidate)



'''
nums = [int(x) for x in input("Enter the array:").split()]
print (nums)
maximum = 0
for i in range(len(nums)):
    counter = nums[i]
    count = 0
    for j in range(len(nums)):
        if(nums[j]==counter):
            count = count + 1
        if maximum < count:
            maximum = count
            maxis = counter

print("Element", maxis , "appears", maximum, "times")
'''