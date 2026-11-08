"""
RECORD CHECK  -  my version
===========================

Name  :Nqobile Mbal'enhle Mpofu 
Lane  : Cyber 
Date  :11/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    """Returns status based on percent"""
    if percent >=100:
        return("OVER LIMIT")
    elif percent >=90:
            return("WARNING")
    else:
            return("OK") 


def check(value,limit):
    """This will reurn the difference and the percentage"""     

    difference=(limit-value)
    percent=(value/limit*100)
    return difference,percent
    

def print_report(label,value,limit,difference,percent, status):
    """This will print the report"""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Value:{value}")
    print(f"Label:{limit}")
    print(f"Difference:{difference}")
    print(f"Percentage:{percent:.2f}%")
    print(f"Status:{status}")
    print("="*34)

    
        
#collecting user input
label =(input("Please enter your Name,Hostname, and IP"))
value = (float(input("Please enter the first number")))
limit =(float(input("Please enter the second number")))

#calculating result, detrminin status 
difference,percent=check(value,limit)
status=status_of(percent)

#final report 

print_report(label,value,limit,difference,percent,status)




