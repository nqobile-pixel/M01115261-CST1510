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

label = input("please enter your name, hostname, and ip address: ")
first = float(input(" Please enter the first value: "))
second = float(input("Please enter the second value: "))

difference = 0.0   # 
percent = 0.0      # 

difference = (first - second)
percent = ( second/ first ) * 100 


print(f" The difference is {difference} and the percentage is {percent:.2f}%")
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here



print(f"  Difference: {difference :>10.2f}")
print(f"  Percentage: {percent :>10.2f}%")
print(f" The two values differ by {difference:>+10.2f}")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
