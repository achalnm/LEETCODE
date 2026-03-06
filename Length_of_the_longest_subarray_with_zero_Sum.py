#nums = [int(x) for x in input("Enter the array: ").split()]

nums = [9, -3, 3, -1, 6, -5]
print("The array is: ", nums)

sum_index_map = {}
curr_sum = 0
max_len = 0

for i in range(len(nums)):
    curr_sum = curr_sum + nums[i]

    if curr_sum == 0:
        max_len = max(max_len, i - 0 + 1)
        print(f"Zero-sum subarray found from index 0 to {i}")

    if curr_sum in sum_index_map:
        previous_index = sum_index_map[curr_sum]
        subarray_length = i - previous_index
        if subarray_length > max_len:
            max_len = subarray_length
            print(f"Zero-sum subarray found from index {previous_index + 1} to {i}")
    else:
        sum_index_map[curr_sum] = i

print("Length of longest zero-sum subarray:", max_len)



'''
nums = [int(x) for x in input("Enter the array: ").split()]
print("The array is: ", nums)

counter = 0
max_len = 0


for i in range(len(nums)):
    counter = 0
    for j in range(i, len(nums)):
        counter = counter + nums[j]
        if (counter == 0):
            max_len = max(max_len, j - i + 1)
            print(f"Zero found from index {i} to {j}")

print("length of subarray", max_len)
'''            

