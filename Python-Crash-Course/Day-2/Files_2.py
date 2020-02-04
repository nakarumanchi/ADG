# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0.0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        pos = line.find('.')
        tot += float(line[pos-1:])
        count = count+1

avg = tot/count
print("Average spam confidence:",avg)
