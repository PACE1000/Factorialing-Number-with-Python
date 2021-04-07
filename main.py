a =int(input("Input the Number : "))
b=1
if a==0:
    print("The Factorial is 1")
elif a==1:
    print("The Factorial is 1")
elif a>=2:
    for x in range (1, a+1):
        b = b*a
print("The Factorial is ", b)
