n = 8

if(n<=2):
    print(n)
    exit()

a = 1
b = 2

for i in range(3, n+1):
    c = a + b
    a = b
    b = c
    
print(b)