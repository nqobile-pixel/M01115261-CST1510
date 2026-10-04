"""
RECORD CHECK  -  my version
===========================

Name  : Nqobile Mpofu
Lane  : Cyber 
Date  :04/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = ""      # replace with an input() call
value = 0.0     # replace with an input() call, converted with float()
limit = 0.0     # replace with an input() call, converted with float()


label = input("please enter your name, hostname, and ip address: ")
first = float(input(" Please enter the first value: "))
second = float(input("Please enter the second value: "))

difference = 0.0   # replace with your calculation
percent = 0.0       # replace with your calculation

difference = (first - second)
percent = ( second/ first ) * 100 

print(f" Your personal details are: {label}")
print(f" The difference is {difference} and the percentage is {percent:.2f}%")

status = ""   # replace with your if / else (or if / elif / else)

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"   

print(f" The status is: {status}")
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  first value: {first :>10.2f}")
print(f"  second value: {second :>10.2f}")
print(f"  Status: {status :>10}")
print(f"  Difference: {difference :>10.2f}")
print(f"  Percentage: {percent :>10.2f}%")

print("=" * 34)

#Got confused with the loop, stoppedat Typical


