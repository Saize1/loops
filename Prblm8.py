num=int(input("Enter your number"))
x=0
y=1
z=0
while(z<=num):
    x=y
    y=z
    z=x+y

print(z)