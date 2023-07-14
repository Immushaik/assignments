#insert function

# l=[10,20,40,30,60,50]
# l.insert(2,30)
# print(l)

# l=[10,20,40,30,60,50]
# l.insert(2,"imran")
# print(l)

# l=[10.30,"aman",40,"imran",60,50.22]
# l.insert(-1,44.44)
# print(j)

# l=[10,20,40,30,60,50]
# l.insert(-3,"imran")
# print(l)

# l=[10,20,40,30,60,50] #When we specify index wich is not part of list that idex value insert at end index
# l.insert(9,100)
# print(l)

#Count function

# l=[50,30,19,33,20,30]          
# print(l.count(30))

# l=[50,30,19,33,"ammi",30,"ammi"]
# print(l.count("ammi"))

# l=[50,30,19,33,"ammi",30,"ammi"] # when we specify element wich is not part of the list, it returns "0" as result
# print(l.count(100))

# l=[44,55,33,11,88] # we can pass only one argument in count of funcion, we can't pass multiple arguments, if we pass it returns Type error
# print(l.count(1,3))

# l=[20,10,30,20.77,60,20.77]
# print(l.count(20.77))

#Index funcion

# l=[20,10,30,20.77,60,20.77] #if we specify element wich is not part of the list, it returns value error
# print(l.index(0))

# l=[20,10,30,20.77,60,20.77]
# print(l.index(20))

# l=[20,10,30,20.77,60,20.77] # if we specify element wich is repeated first occur element will retuen by index function
# print(l.index(20.77))

# l=[20,10,30,20.77,60,20.77] # if we pass argument which is not part of a list, it returns value error
# print(l.index(100))

#append funcion

# l=[50,30,19,33,"ammi",30,"ammi"]
# l.append(20)
# print(l)

# l=[50,30,19,33,"ammi",30,"ammi"] # if we add list of elements using append, whole list elemnts added as one element at end index, it looks like a nested list
# h=[20,30,40]
# l.append(h)
# print(l)

# l=[50,30,19,33,"ammi",30,"ammi"] 
# l.append("imran")
# print(l)

#Extend function

# l=[50,30,19,33,"ammi",30,"ammi"] # if we pass int datatype as argument it returns type error
# l.extend(30)
# print(l)

# l=[50,30,19,33,"ammi",30,"ammi"] #if we pass string it covert and takes as characters
# l.extend("imran")
# print(l)

# l=[50,30,19,33,"ammi",30,"ammi"]
# l1=[45,55,67]
# l.extend(l1)
# print(l)

# l=[50,30,19,33,"ammi",30,"ammi"] #Float datatype not acceplable,returns Type error
# l.extend(30.4)
# print(l)

#Sort function

# l=[50,30,19,33,"ammi",30,"ammi"] # we can't sort list of int and string datatypes
# l.sort()
# print(l)

# l=[50,30,19,33,30,88.99]
# l.sort()
# print(l)

# l=["imran","aman","suneel","pradeep"]
# l.sort()
# print(l)

#Reverse function

# l=[50,30,11,20,44]
# l.reverse()
# print(l)

# l=[50,"imran",40,"suneel","pavan"]
# l.reverse(50)
# print(l)

#pop function

# l=[50,"imran",40,"suneel","pavan"] #whwn we specify element which is not part of list, it returns index error
# print(l.pop(100))

# l=[50,"imran",40,"suneel","pavan"]
# l.pop(1)
# print(l)

l=[50,"imran",40,"suneel",10]
l.pop()
print(l)
