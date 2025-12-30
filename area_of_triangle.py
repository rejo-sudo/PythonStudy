"""
When all the sides are known of the triangle
a, b, c

semi perimeter (s) = a + b + c / 2
Area = square root of (s * (s-a) * (s-b) * (s-c))

"""

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of the triangle of the give side is: ", round(area, 2))







