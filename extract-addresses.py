fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
  words = line.split()
  # have to check that len(words)>0 otherwise throws out of range error on blank lines
  if len(words) and words[0] == "From":
    print(words[1])
    count +=1
print("There were", count, "lines in the file with From as the first word")
