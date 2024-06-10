def my_function(c):
    if c.isupper():
        print("uppercase alphabet")
    elif c.islower():
        print("lowercase alphabet")
    else:
        print("not an alphabet")
c=input("enter the character:")
my_function(c)