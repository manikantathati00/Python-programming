def my_function(first,second):
    temp=first
    first=second
    second=temp
    print("after swapping first number =",first)
    print("after swapping second number =",second)
first=int(input("enter the first number:"))
second=int(input("enter the second number:"))
my_function(first,second)