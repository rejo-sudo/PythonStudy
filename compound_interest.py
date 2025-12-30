"""
Amount = p * (1+r/100) ** T
ci = Amt - p
"""

prin = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time duration: "))

amt1 = prin * (1 + rate/100) ** time
amt2 = prin * pow((1 + rate/100), time)
print(amt1, amt2)
print(round(amt2,2))

ci = amt2 - prin
print("Compound interest: ", round(ci))

