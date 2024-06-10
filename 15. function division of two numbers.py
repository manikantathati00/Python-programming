def my_function(n1,n2):
    if n2!=0:
        quotient=n1/n2
        print("division of two numbers =",quotient)
    else:
        print("error!")
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
my_function(n1,n2)