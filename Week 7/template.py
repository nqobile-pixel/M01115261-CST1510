"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :    Cyber
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line (raw_line):
    """Cleans a messy security record,stores in in a dict """
   
    pieces=raw_line.split(",")
    mydict={}
    for piece in pieces:
    
            key, value = piece.split("=")  #separates each key and valu 
            key = key.strip().lower()
            value = value.strip()

    

    if key == "attempts":
            value = int(value) #converting the attempt sto a number 

    mydict[key] = value

    return mydict


def status_of(attempts, result):
    """Checks whether a security record needs attention."""

    # Check if the result failed and the attempts reached the threshold
    if result.lower() == "failed" and attempts >= 10:
        return "FLAGGED"
    else:
        return "OK"



# A few security records with different spacing and capitalisation================= INPUT ====================

raw_records = [
    " SrC=10.0.0.5,atTEMPTS=12,RESULT=FAILED",
    "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED",
    "src=10.0.0.5,Attempts=12,result=failed",
    "SRc=10.0.0.5,ATtemPTS=12,RESULT=fAILED",
    "srC=10.0.0.5,ATTEMPTS=12,result=FAILED"
]



flagged_count = 0


for raw_record in raw_records: #goes through esch record 

    record = parse_line(raw_record)


    status = status_of(record["attempts"], record["result"]) #gets status from attempts and results

    print(record)
    print("Status:", status)

   
    if status == "FLAGGED":
        flagged_count += 1 #counting how many attempts are flagged 


# report
print ("=")*34
print("Total records:", len(raw_records))
print("Flagged records:", flagged_count)
print ("=")*34

#Error, didn't runs