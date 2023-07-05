# n=int(input("Enter your no:"))
# for i in range(n+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(n):
#     for j in range(1,n-i):
#         print(" ",end="")
#     for h in range(0,i+1):  
#         print("*",end="")
#     print()  

# for i in range(n):
#     for h in range(0,i): 
#         print(" ",end="")  
#     for j in range(i,5):
#         print("*",end="")
#     print()

# for i in reversed(range(n)):
#     for j in range(i+1):
#         print("*",end="")
#     print()  

for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print(j, end='')
    print()
