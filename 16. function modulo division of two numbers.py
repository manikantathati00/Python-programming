def my_function(n1,n2):
    if n2!=0:
        remainder=n1%n2
        print("modulo division of two numbers =",remainder)
    else:
        print("error!")
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
my_function(n1,n2)
