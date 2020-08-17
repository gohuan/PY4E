#8.4 Open the file romeo.txt and read it line by line. For each line, 
#split the line into a list of words using the split() method. The program 
#should build a list of words. For each word on each line check to see if 
#the word is already in the list and if not append it to the list. When the 
#program completes, sort and print the resulting words in alphabetical order.

handle = input("File Name:")
handle1 = open(handle)

path = list()
for w in handle1:
    for m in w.split():
        if m not in path:
            path.append(m)
            
path.sort()
print(path)