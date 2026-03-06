nums = [int(x) for x in (input("Enter the numbers:").split())]
print("The array is: ", nums)

result = 0
for i in nums:
    result = result^i
print(result)



'''
nums = [int(x) for x in (input("Enter the numbers:").split())]
print("The array is: ", nums)

counter  = 0
seen = set()
for i in range(len(nums)):
    counter = nums[i]
    if counter in seen:
        continue
    count = 0
    for j in range(i, len(nums)):
        if (counter == nums[j]):
            count = count + 1
    if (count == 1):
         print(counter, "appears once")
    seen.add(counter)
'''