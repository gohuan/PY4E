#3.1 Write a program to prompt the user for 
#hours and rate per hour using input to compute 
#gross pay. Pay the hourly rate for the hours up 
#to 40 and 1.5 times the hourly rate for all hours 
#worked above 40 hours. Use 45 hours and a rate of 
#10.50 per hour to test the program (the pay should 
#be 498.75). You should use input to read a string 
#and float() to convert the string to a number. 
#Do not worry about error checking the user input 
#- assume the user types numbers properly.

hour = input("What is the hours worked:")
rate = input("What is the wage rate:")

hr = float(hour)
rt = float(rate)

if hr > 40:
    hw = hr - 40
    he = hw*1.5
    ha = he + 40
    pay = ha * rt
else:
    pay = hr * rt
    
print(pay)
    