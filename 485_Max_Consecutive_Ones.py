nums = [int(x) for x in (input("Enter the array seperated by spaces: ").split())]
print ("The array is:", nums)
m = 0
i=0
count = 0
for i in range(len(nums)):
    if nums[i] == 1:
        count += 1
        m = max(m, count) 
    else:
        count = 0        
print("The numbers of consecutive 1s are:", m)

        
    
    