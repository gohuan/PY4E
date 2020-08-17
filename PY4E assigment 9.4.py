#9.4 Write a program to read through the mbox-short.txt and figure 
#out who has sent the greatest number of mail messages. The program 
#looks for 'From ' lines and takes the second word of those lines as 
#the person who sent the mail. The program creates a Python dictionary 
#that maps the sender's mail address to a count of the number of times 
#they appear in the file. After the dictionary is produced, the program 
#reads through the dictionary using a maximum loop to find the most prolific 
#committer.
#cwen@iupui.edu 5


file = input("Input file name:")
close = open(file)

counts = dict()
for item in close:
    item = item.rstrip()
    if not item.startswith("From:") : continue
    split = item.split()
    counts[split[1]] = counts.get(split[1], 0) + 1
        
bigname = None
bigcount = None
for e,b in counts.items():
    if bigname is None or b > bigcount:
        bigname = e
        bigcount = b
print(bigname, bigcount)
    