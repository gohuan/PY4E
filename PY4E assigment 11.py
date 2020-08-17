import re

opn = open("regex_sum_742233.txt")

lst = list()
for item in opn:
    item.rstrip()
    item = re.findall("[0-9]+", item)
    if len(item) > 0:
        lst = lst + item
    #print(lst)

count = 0
for lines in lst:
    lines = int(lines)
    count = count + lines
    
print(count)