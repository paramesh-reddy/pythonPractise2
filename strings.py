#
# string in arrays

x= 'hello'
for s in  x:
  print(s+s, end=" ")
  
  #string in functions 
  # len, .in , .not, .upper ,.lower,.strip, .replace,.split 
  
x = (input ("enter ur channel"))
print(len(x))
if "ua" not in  x :
    print ("yes") 
# else :
#     print ('no')    
    
    print (x.upper())
    print (x.lower ())
    print (x.strip()) 
    print (x.replace("qu", 'ua'))
    print (x.split(" "))
    print ( x[2:3])
    print(x)
    