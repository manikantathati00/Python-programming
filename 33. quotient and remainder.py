dividend=int(input("enter the dividend value:"))
divisor=int(input("enter the divisor value:"))
if divisor!=0:
    quotient=dividend/divisor
    remainder=dividend%divisor
    print("quotient=",quotient)
    print("remainder=",remainder)
else:
    print("error")