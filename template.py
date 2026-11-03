"""
RECORD CHECK  -  my version
===========================

Name  : Nqobile Mpofu
Lane  :  / Cyber    (delete two)
Date  : 11/3/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(value, limit):
    """Calculate the difference, percentage and status for a record."""
    if limit == 0:
        raise ValueError("Limit cannot be zero.")

    difference = limit - value
    percent = (value / limit) * 100
    

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status



def print_report(label,value,limit,difference,percent, status):
    """Prints a report showing a records label, value, limit, difference, percentage and status."""
    print("=" * 34)
    print(f" RECORD CHECK- {label}")
    print("=" * 34)
    print(f"Value:{value}")
    print(f"Label:{label}")
    print(f"Difference:{difference}")
    print(f"Percentage:{percent:.2f}%")
    print(f"Status:{status}")
    print("="*34)



def load_records(path):
    """Load records from a file and return a list of dicts."""
    records = []
  
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(',')
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
                })
            
    return records

load_records("records_sample.txt")
new_records = load_records("records_sample.txt")
print(new_records)
print("Records loaded successfully.")
 


   




count_over_limit = 0  # Initialize a counter for OVER LIMIT records
for record in new_records:   #going through each record in the list of records
    label = record["label"]
    value = record["value"]
    limit = record["limit"]

    difference, percent, status = check_record(value, limit)
    print_report(label, value, limit, difference, percent, status) #passing the arguments to print_report
    if status == "OVER LIMIT":
        count_over_limit += 1
print(f"Number of records over limit: {count_over_limit}")


