x = int(input("Enter an integer: "))

xcopy = x
reverse = 0

if x < 0:
    print("Negative numbers, pallindrome nono")

while x > 0:
    reverse = (reverse * 10) + (x%10)
    x = x // 10

if (reverse == xcopy):
    print("Yes, Pallindrome found")
    
else:
    print("not a pallindrome")