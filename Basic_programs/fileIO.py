fd = open("numbers.txt", 'w')
fd.writelines(["This is block one\n",
               "This is block two\n",
               "This is block three....................\n",
               "This is block four\n",
               "This is block five\n",
               "This is block six\n"]
              )
fd.close

fd = open("numbers.txt", 'r')

for line in fd.readlines():
    if (len(line) > 25):
        print(len(line))
        continue
    print(line.upper(), end="")
fd.close()

with open("numbers.txt", 'r') as fd:
    for line in fd.readlines():
        if (len(line) > 25):
            print(len(line))
            continue
        print(line.upper(), end="")
