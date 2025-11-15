file1 = ('Codingal2.txt', 'r')
file2 = ('Codingal.txt', 'w')
file = file1.readlines()

for line in file:
    if not (line.startswith('Coding')):
        print (line)

        file2.write(line)

file2.close()
file1.close()        