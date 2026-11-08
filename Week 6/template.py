"""
RECORD CHECK  -  my version
===========================

Name  :Nqobile Mpofu 
Lane  :  Cyber 
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""




import pandas as pd

# Create a dictionary containing the dat
data = {
    "label": ["A", "B", "C", "D", "E", "F"],
    "value": [10, 25, 15, 30, 18, 12],
    "limit": [20, 20, 20, 25, 20, 15]
}

 # Convert dictionary into DataFrame
df = pd.DataFrame(data)



# Calculate percentage for each row
df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x > 90 else "OK")



import matplotlib.pyplot as plt
print(df[["limit", "percent", "status"]])
not_okay = df[df["status"] != "OK"]   # Filter records that are not OK
print(not_okay) 

# Count records in each status group
grouped = df.groupby("status").size() #Size prints the number of rows in each group
print(grouped)
 # Save DataFrame to CSV
df.to_csv("status_counts.csv",index=False)

# Create a bar chart showing status counts
df["status"].value_counts().plot(kind="bar")
plt.title("Status of Values")
plt.xlabel("Status")
plt.ylabel("Count")
plt.savefig("status_counts.png") # Saves chart as image
plt.show()# Displays the  chart


