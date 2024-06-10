def my_function(c):
    if c>='A'and c<='Z':
        print("uppercase alphabet")
    elif c>='a'and c<='z':
        print("lowercase alphabet")
    else:
        print("not alphabet")
c=input("enter the character:")
my_function(c)