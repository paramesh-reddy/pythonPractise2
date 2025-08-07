# vegetables =['bringel','tomato','onion','carraot','drumstick']
# fruits=['apple','mango','bannana','orange']
# print (vegetables[len(vegetables)-1])

# vegetables.append('dosakaya')

# vegetables.insert(0,'mullangi')
# vegetables.extend(fruits)
# vegetables.pop(0)
# vegetables.reverse()
# # vegetables.clear()

# print(vegetables)


numbers=[1,2,3,4,5,6,78,90,79,89,98,676]
ans = 0     
for x in numbers:
    if x > ans:
        ans = x
print (ans)
