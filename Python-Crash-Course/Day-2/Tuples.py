name = "mbox-short.txt"
handle = open(name)

names = dict()

for lines in handle:
    lines = lines.rstrip()
    if lines == "" or not lines.startswith("From "):
        continue
    words = lines.split()
    word = words[5].split(":")
    names[word[0]] = names.get(word[0],0)+1
tup = names.items()
tup.sort()
for k,v in tup :
    print(k,v)
