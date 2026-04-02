list1 = [1,2,4]
list2 = [1,3,4]

i = j = 0
result = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

result.extend(list1[i:])
result.extend(list2[j:])

print(result)