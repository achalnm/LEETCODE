# Input two arrays
n1 = [int(x) for x in input("Enter array 1: ").split()]
m1 = [int(x) for x in input("Enter array 2: ").split()]

# Take union using set
union_set = set(n1) | set(m1) 

# Convert back to sorted list
union_list = sorted(list(union_set))

print("Union of two arrays:", union_list)



'''
n1 = input("Enter the array1 seperated by spaces: ").split()
n1 = [int(x) for x in n1]

m1 = input("Enter the array2 seperated by spaces").split()
m1 = [int(x) for x in m1]

n1.sort()
m1.sort()

print("Sorted Array 1 is: ", n1)
print("Sorted Array 2 is: ", m1)

n = len(n1)
m = len(m1)

newarr = n1 + m1
print (newarr)
i=0

while i < len(newarr):
    if newarr[i] in newarr[:i]:
        newarr.pop(i)
    else:
        i = i+1
newarr.sort()

print (newarr)

'''
            
    










        
        