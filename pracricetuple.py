  

#tuple
t=(1,2,3,)
print ("First Element is ",t[0])


#tuple check 
t =(1,2,3)
x=2
ans = x in t
print (ans)


#convert
list =[1,2,3]
mytuple = tuple(list)
print (mytuple)


# multiple list 
list1 = [1, 2]
list2 = ['a', 'b']

mytuple = tuple(zip(list1, list2))
print(mytuple)

# sum 
t = (10, 20, 30)
total = sum(t)
print( total)

