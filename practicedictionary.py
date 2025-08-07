
# frequency 
# numbers=[1,2,2,3,1]
# frequency ={}
 
# for num in numbers:
#      if num in frequency:
#          frequency[num] +=1
         
#      else:
#          frequency[num]=1
# print(frequency)



from collections import Counter

numbers = [1, 2, 2, 3, 1]
frequency = Counter(numbers)

print(frequency)

#max value  
x= {"a":10, "b":5,"c":12}

max_value= max(x)
 
print (max_value)

# merge
x = {"a":1}
y = { "b":2}
merged = x | y 
print (merged)

#swap

Input= {'a': 1, 'b': 2}
x= {value:keys for keys, value in Input.items()}
print(x)


# equal

x={"a":1}
y={"a":1}

equal =  x== y
print (True)

 