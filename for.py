"""num = int(input("Enter Value"))
a = 0
b = 1
total = 0
print("Series",a,b)
total = a + b
while(total <= num):
    print(total)
    a = b
    b = total
    total = a + b"""

num = int(input("Enter Value"))
a = 0
b = 1
total = 0
for i in range(1, num):
    print(a)
    total = a + b
    a = b
    b = total
