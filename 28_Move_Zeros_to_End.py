nums = input("Enter the numbers seperated by spaces: ").split()
nums = [int(x) for x in nums]
print ("The array entered is: ", nums)

n = len(nums)
print ("length of the array is: ", n)

last = 0

for i in range(n):
    if (nums[i] != 0):
        nums[i], nums[last] = nums[last], nums[i]
        last = last + 1
        
print ("After moving zeroes: ", nums)
       
        