from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        '''
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Check for a "drop"
                count += 1
                if count > 1:  # More than 1 drop → not rotated sorted
                    return False
        return True
        ''' 
        for i in range(n-1):
            if nums[i] > nums[i + 1]: 
                count += 1
            elif nums[i] < nums[i + 1]:
                continue
        if nums[n-1] > nums[0]:
                count +=1
        if count > 1:  
                return False
        else:
                return True
       
        


if __name__ == "__main__":
    s = Solution()
    
    # Take custom input from user
    nums = input("Enter numbers separated by spaces: ").split()
    nums = [int(x) for x in nums]
    
    # Call the function and print result
    print(s.check(nums))