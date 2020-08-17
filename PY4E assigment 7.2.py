#7.2 Write a program that prompts for a file name, then opens 
#that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of 
#the lines and compute the average of those values and produce an output 
#as shown below. Do not use the sum() function or a variable named sum in 
#your solution.

fname = input("Input file name:")

try:
    fhand = open(fname)
except:
    print("Unavaliable")
    
count = 0
add = 0
avg = 0
for item in fhand:
    #Remove /n
    item = item.rstrip()
    if not item.startswith("X-DSPAM-Confidence:") : continue
    #print(item)
    colon = item.find(":")
    colon1 = item[colon+1:]
    colon2 = float(colon1)
    #print(colon2)
    count = count + 1
    #print(count)
    add = add + colon2
    #print(add)
    avg = add / count
    #print(avg)
print("Average spam confidence:", avg)