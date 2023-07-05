#slicing 
a="i am working in marolix as a python developper"
# print(a[:]) #or
# print(a[::]) #bot prints same output
# print(a[::1]) #return elements in positive direction
# print(a[::-1]) #return elements in negative direction
# print(a[-1:5:-1])
# print(a[4:-8:2])
# print(a[-4:-9:-1])
# print(a[8:20:4])
# print(a[-3::-3]) #it prints upto end of the sequence(Default value is 1 if we not provide any value)
# print(a[:20:6]) #it prints from starting position(Default value is 1 if we not provide any value)
# print(a[5:-7:-3]) #Returns empty because it goes in negative direction,it dosn't start with positive value 
# print(a[-1:8:1]) #Returns empty because it goes in positive direction,it dosn't start with negative value 
# print(a[-4:10:-2])
# print(a[5:-1:5])
# print(a[15:25:3])
# print(a[2:18:1])
# print(a[-5:22:-4])
# print(a[:-10:-3])
# print(a[10::5])
# print(a[5:-10:3])
# print(a[-1:-14:-2])
# print(a[::-10])
# print(a[:-10:])
# print(a[:10:-1])
# print(a[1:-1:])
# print(a[:-1:])
# print(a[:-15:1])
# print(a[10::-1])
# print(a[:-4:2])
# print(a[20::-3])


# 1)Natural numbers
# i=1
# print("Natural numbers")
# while i<=10:
#     print(i)
#     i+=1

# 2)Sum of all given numbers
# n=int(input("pls enter the no:"))
# k=0
# for i in range(1,n+1):
#     k+=i
# print("The sum of all numbers is %s"%k)

# 3)Multiplication table of given number
n=int(input("Enter no:"))
for x in range(1,11):
    print("{}*{}={}".format(n,x,n*x))

# 4)Display numbers from list
# s=[10,40,200,60,70]
# for i in s:
#     print(i)

# 5)Display count of the digits from the numbers
# f=676555
# g=str(f)
# cnt=0
# for i in g:
#     cnt+=1
# print("Total number of digits is",cnt)

# 6)Print list in reverse order
# s=[6,7,2,8,3,7]
# for i in reversed(s):
#     print(i)
#or
# for i in s[::-1]:
#     print(i) 

# 7)Display numbers -10 to -1 using for loop
# n=10
# for i in range(0,n):
#     print(i-n)

# 8)Execute else block after succesful execution of for loop
# for i in range(5):
#     print(i)
# else:
#     print("Done")    

# 9)Display prime numbers
# for i in range(2,20+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)   


# 10)fibonacci series
# def arg():
#     n,n1=0,1
#     for i in range(6):
#        yield n
#        n,n1=n1,n+n1
       
# ob=arg()
# for i in range(6):
#   print(next(ob))










