#5.2 Write a program that repeatedly prompts a user for integer 
#numbers until the user enters 'done'. Once 'done' is entered, print 
#out the largest and smallest of the numbers. If the user enters anything 
#other than a valid number catch it with a try/except and put out an 
#appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and
#match the output below.


smallest = None
largest = None

while True:
    prompt = input("Input number, 'done' when finished:")
    if prompt == 'done':
        break
    
    try:
        anum = int(prompt)
    except:
        print("Invalid input")
        continue
    
    if largest is None:
        largest = anum
    if smallest is None:
        smallest = anum
    if anum > largest:
        largest = anum
    if anum < smallest:
        smallest = anum
    
    
print("Maximum is:", largest)
print("Minimum is:", smallest)
