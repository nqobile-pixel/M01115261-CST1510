"""
RECORD CHECK  -  my version
===========================

Name  :Nqobile Mpofu
Lane  : Cyber      
Date  :08/01/2006

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = ""      # : replace with an input() call
first = 00.0     # : replace with an input() call, converted
second = 00.0  # : replace with an input() call, converted

#Asks for user input and assigns them in variables.
label = input("please enter your name, hostname, and ip address: ")
first = float(input(" Please enter the first value: ")) #Converts the user input into float
second = float(input("Please enter the second value: ")) ##Converts the user input into float
      

difference = (first - second)  #Calculating the difference
percent = ( second/ first ) * 100  #Calculating the precentage 

#Making the report 

print(f" The difference is {difference} and the percentage is {percent:.2f}%") #Printing out the variable of difference, and percent to 2 decimal places 
print()
print("=" * 34) #Making a separator
print(f"  RECORD CHECK  -  {label}") #Naming RECORDCHECK 
print("=" * 34)
print(f"  Difference: {difference :>10.2f}") #prints the difference right alligned (10 spaces) and to two decimal points 
print(f"  Percentage: {percent :>10.2f}%") #
print(f" The two values differ by {difference:>+10.2f}") #prints the difference right alligned (10 spaces) and to two decimal points 
print("=" * 34)



