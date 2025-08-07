# sum

numbers=[1,2,3,4]

# print(len(numbers))

# total= sum(numbers)
# print(total)
total= 0
for num in numbers:
     total += num
     
print(total)
 # max , min 

x = [7,3,9,1]

maxima= max(x)
minima = min(x)
print ( "maxima:",maxima,)
print ("minima:",minima)

#remove dupilicate
x = [1,2,3,2,1]
number = list(set(x))

print(number)

#reverse
x=[1,2,3]

x.reverse()
print(x)


#A palindrome is something that reads the same forward and backward.



def palindrome(lst):
    return lst == lst[::-1]
numbers = [1,2,3,4,3,2,1,]

if palindrome(numbers):
    print("True")
else:
    print("False")
    
    
    