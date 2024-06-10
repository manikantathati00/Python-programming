def my_function(radius):
    pi=3.14
    area=pi*radius**2
    perimeter=2*pi*radius
    print("area of circle =",area)
    print("perimeter of circle =",perimeter)
radius=float(input("enter the radius value:"))
my_function(radius)