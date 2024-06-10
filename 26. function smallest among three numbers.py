def my_function(n1,n2,n3):
    if n1<=n2 and n1<=n3:
        print("smallest =",n1)
    elif n2<=n1 and n2<=n3:
        print("smallest =",n2)
    else:
        print("smallest =",n3)
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))
my_function(n1,n2,n3)