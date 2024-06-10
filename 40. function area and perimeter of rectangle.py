def my_function(length,breadth):
    area=length*breadth
    perimeter=2*(length+breadth)
    print("area of rectangle =",area)
    print("perimeter of rectangle =",perimeter)
length=int(input("enter the length value:"))
breadth=int(input("enter the breadth value:"))
my_function(length,breadth)