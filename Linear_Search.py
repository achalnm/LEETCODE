nums = input("Enter the numbers seperated by spaces: ").split()
nums = [int(x) for x in nums]
count = 0
n = len(nums)

print("Enter the search element: ")
s = int(input())

for i in range(n):
    if (nums[i]== s):
        print("value", s ,"found at", i+1, "position")
        count = 1
        break;

if (count != 1):
    print("Search element not found")
