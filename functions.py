# def addition(num1,num2):
#     print(num1 + num2)
# addition(5,6)

#recursion
def addition (n):
    if(n==0):
        return 0
    return n + addition(n-1)
print(addition(10))