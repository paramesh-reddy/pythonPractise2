#ForLoop, WhileLoop

#purpose : Repeats as long as a conditon true

'''
i = 1
while i < 7:
    if i%2 == 0:
        i += 1
    #continue
    break
print (i)
i+= 1

'''
x = int (input('enter the number'))

for i in range( 1,11):
     print(f"{x} * {i} = {i*x}")