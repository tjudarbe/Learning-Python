fname = input("Enter a file name: ")
try:
    fhand = open(fname, "r")
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
average = 0
total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(' ')
        number = line[pos:].rstrip()
        number = float(number)
        count = count + 1
        total = total + number
        average = total / count

print(average)
