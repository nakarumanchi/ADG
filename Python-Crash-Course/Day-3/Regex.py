import re

fname = "Data.txt"
fhand = open(fname)
sum = 0
lst = list()
for lines in fhand:
    lines = lines.rstrip()
    if lines is "":
        continue
    y = re.findall('[0-9]+',lines)
    if len(y) == 0 :
        continue
    lst = lst + y
#    print(lines)
print(lst)
for no in lst:
    sum = sum + int(no)
print(sum)
