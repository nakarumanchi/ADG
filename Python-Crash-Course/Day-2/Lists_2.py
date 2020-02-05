fname = input("Enter a file name:")
fh = open(fname)
count = 0
for lines in fh:
    lines = lines.rstrip()
    if lines.startswith("From ") :
        temp = lines.split()
        print(temp[1])
        count = count+1
    else :
        continue


print("There were", count, "lines in the file with From as the first word")
