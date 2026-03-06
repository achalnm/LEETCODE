nums = [int(x) for x in input("Enter the array: ").split()]

candidate = None
count = 0

for num in nums:
    if count == 0:
        candidate = num
    count = count + (1 if num == candidate else -1)
    
        
    
print(candidate)