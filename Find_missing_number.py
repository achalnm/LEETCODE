#nums = [int(x) for x in input("Enter the array elements separated by spaces: ").split()]
nums = [1,2,3,7,8,9,15]
n = len(nums)
high = nums[0]
print("length of array is: ", n)

for i in range(n):
    if nums[i] > high:
        high = nums[i]
   
miss = []
     
if (n != high):
    print("Elements missing")
    for i in range(1, high+1):
        if i not in nums:
            miss.append(i)
    print("missing numbers are", miss)
    full = miss + nums
    full.sort()
    print("Full list is:", full)
          
else:
    print("All elements exist")

    
'''
# Input array
# nums = [int(x) for x in input("Enter the array elements separated by spaces: ").split()]
nums = [1, 2, 3, 7, 8, 9, 15]

# Step 1: Find the maximum value
high = max(nums)

# Step 2: Convert list to set for fast lookup
nums_set = set(nums)

# Step 3: Find missing numbers
miss = [i for i in range(1, high + 1) if i not in nums_set]

if miss:
    print("Elements missing")
    print("Missing numbers are:", miss)
else:
    print("All elements exist")

# Step 4: Combine original array and missing numbers, then sort
full_list = sorted(nums + miss)
print("Full list is:", full_list)
'''
    
    