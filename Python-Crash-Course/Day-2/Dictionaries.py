name = "mbox-short.txt"
handle = open(name)

names = dict()

for lines in handle:
    lines = lines.rstrip()
    if lines == "" or not lines.startswith("From "):
        continue
    words = lines.split()
    names[words[1]] = names.get(words[1],0)+1
bigword = None
bigno = None
for k,v in names.items() :
    if bigno is None or bigno < v:
        bigword = k
        bigno = v
print(bigword, bigno)
