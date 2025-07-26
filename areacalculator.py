#first we code the shape chooser
print("1=square, 2=rectange, 3=triangle, 4=circle")
num = int(input("Enter the number corresponding to the chosen shape"))
if num==1:
    a = int(input("Input side length"))
    print(f"The area of the square is {a**2}")
elif num==2:
    b = int(input("Input length"))
    c = int(input("Input width"))
    print(f"The area of the rectangle is {b*c}")
elif num==3:
    d = int(input("Input height"))
    e = int(input("Input base"))
    print(f"The area of the triangle is {0.5*e*d}")
elif num==4:
    f = int(input("Input radius"))
    import math
    print(f"The area of the circle is {math.pi*(f**2)}")