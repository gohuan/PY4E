#10.2 Write a program to read through the mbox-short.txt 
#and figure out the distribution by hour of the day for 
#each of the messages. You can pull the hour out from the 
#'From ' line by finding the time and then splitting the 
#string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print 
#out the counts, sorted by hour as shown below.

opses = input("File Name:")
seass = open(opses)

count = {}
for items in seass:
    items = items.rstrip()
    if not items.startswith("From "):
        continue
    items = items.split()
    item = items[5]
    hours = item.split(":")
    count[hours[0]] = count.get(hours[0], 0) + 1

ls = []
for v,k in count.items():
    most = (v,k)
    ls.append(most)

ls = sorted(ls)
for v,k in ls[:]:
    print(v,k)
