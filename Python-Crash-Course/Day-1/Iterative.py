largest = None
smallest = None
ival = 0
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        ival = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None and smallest is None:
        largest = num
        smallest = num
    else:
        if largest < num:
            smallest = num
        elif smallest > num:
            largest = num


print("Maximum is", largest)
print("Minimum is", smallest)
