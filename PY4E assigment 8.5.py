#8.5 Open the file mbox-short.txt and read it line by line. 
#When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in 
#the line (i.e. the entire address of the person who sent the message). 
#Then print out a count at the end.

inp = input("Fine Name:")
item = open(inp)

count = 0
for obj in item:
    obj = obj.rstrip()
    if not obj.startswith("From:") : continue
    
    ect = obj.split()
    print(ect[1])

    count = count + 1
print(count)