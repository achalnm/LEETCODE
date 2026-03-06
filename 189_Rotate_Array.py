
nums = input("Enter numbers separated by spaces: ").split()
nums = [int(x) for x in nums]
k = int(input("Enter k: "))


n = len(nums)
k = k % n  
nums[:] = nums[-k:] + nums[:-k]  

print("The rotated array is:", nums)