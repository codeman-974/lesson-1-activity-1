outputFile = open ('Updatedfile.txt', "w")
inputFile = open ('hello.txt', "r")

lines_seen_so_far = set()
print ("Eliminating duplicate line...")
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()        