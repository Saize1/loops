fruits=['Apple','Watermelon','grapes','mangoes']
for i in fruits:
    print(i)

# range function
# for i in range(1,8):
#     print(i)

# break function
# for i in range(10):
#     print(i)

#     if i==5:
#         break

# continue function
# for i in range(10):
#     if i==5:
#         continue
#     print(i)

# # f string
# num=int(input("enter your number"))
# for i in range(1,11):
#     print(f"{num} X{i}={num*i}")

# star pattern
n=4
for i in range(3):
    print(" "*(n-i-1),end="")
    print(" "*(2*i+1),end="")
    print(" "*(n-i-1))

