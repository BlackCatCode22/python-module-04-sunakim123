#Worked Exercise 7.1
fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())

#Strings, Files, Lists and the Guardian Pattern (Chpt 8)
han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()

    #Guardian pattern
    if len(wds) < 3 or wds[0] != 'From' :
        print(wds[2])

    #2
    print('Words:', wds)
    if wds[0] != 'From':
        print('Ignore')
        continue
    print(wds[2])

    #3
    print('Line:', line)
    wds = line.split()
    print('Words:', wds)
    if len(wds) < 1 :
        continue
    if wds[0] != 'From' :
        print('Ignore')
        continue
    print(wds[2])

    #4
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
