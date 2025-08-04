#if , Else ,Elif , logical operators
"""
x=  int(input('enter ur NUmber:'))
y= int( input ("enter ur number:"))

if x > y :
    print(x)
else: print(y)
"""

'''
x = int (input("enter rating of ismart movies "))
y= int (input ('movie rating of new '))
z= int (input ( 'enter rating new 2'))
if x >y :
    print('i will go to  ismart movie')
    
elif x == y:
     print (' i will go to both movies')
     
else :
    print('i will go to  new movie6')    

'''

x = int (input("enter rating of ismart movies "))
y= int (input ('movie rating of new '))
z= int (input ( 'enter rating new 2'))
if x >y and x>z :
    print('i will go to  ismart movie')
    
elif y>z and y>x :
     print (' i will go to both movies')
     
else :
    print('i will go to  new movies2')    