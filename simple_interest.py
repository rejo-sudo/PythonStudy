"""
Simple interest = (p*r*t)/100
p = principal amount
r = rate of interest
t = time duration

"""

p = float(input("Enter first principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time duration: "))

si = (p*r*t)/100
print("Simple interest: ", si)
