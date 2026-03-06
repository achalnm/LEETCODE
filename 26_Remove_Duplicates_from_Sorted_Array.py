
nums = input("Enter numbers separated by spaces: ").split()
nums = [int(x) for x in nums]

nums.sort()
print ("Array after sorting", nums)


unique_nums = []


for i in range(len(nums)):
    if i == 0:
        unique_nums.append(nums[i])
    else:
        if nums[i] != unique_nums[-1]:  # not a duplicate
            unique_nums.append(nums[i])
        else:
            print("Duplicate removed:", nums[i])

print("Array after removing duplicates:", unique_nums)