nums = [int(x) for x in input("Enter the array: ").split()]
target =  int(input("Enter the target: "))
print(nums)
count = 0
for i in range(len(nums)):
    if (nums[i] == target):
        print("Number found at index ", i)
        count = 1

if (count != 1):
    print ("Number not found")
    

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
'''

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0           
        r = len(nums)-1  
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
'''