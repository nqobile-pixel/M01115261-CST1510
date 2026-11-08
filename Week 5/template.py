"""
RECORD CHECK  -  my version
===========================

Name  : Nqobile Mpofu
Lane  : Cybersecurity
Date  : 25/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



class Record:
    over_limit_count=0

    def __init__(self,label,value,limit):
        """Initialising a record with it's label,value, and limit"""
        self.label = label
        self.value = value 
        self.limit = limit 
        if self.value>=limit:
            Record.over_limit_count+=1  # Increase the  counter if over limit

    
    def percent(self ):
        """Returns value as a percentage of limit"""
        return (self.value/self.limit)*100

    
    def status(self):
        """Returns OK,WARNING,OR OVER LIMIT depending on the conditions"""
        percentage = self.percent()

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage  >= 90: 
            return "WARNING"
        else:
            return "OK"

# Creates  a list of Record objects
records = [ 
    Record("R-001", 87.0,100.0),
    Record("R-002", 120.0,100.0), 
    Record("R-003", 95.0,100.0) 
]   

# making a list of Record objects
for record in records:
    print (record.status())



# printing a formatted report for each record
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"Label: {record.label} Value: {record.value} Limit:{record.limit}")
    print (record.status())
    print("=" * 34)




