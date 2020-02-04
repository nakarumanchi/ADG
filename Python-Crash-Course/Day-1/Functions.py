def computepay(h,r):
    pay = 0.0
    if h <= 40:
        pay = h*r
        return pay

    pay = 40*r
    h -= 40
    pay += (h*1.5*r)
    return pay


hrs = float(input("Enter Hours:"))
rph = float(input("Enter rate per hour:"))

p = computepay(hrs,rph)
print(p)
