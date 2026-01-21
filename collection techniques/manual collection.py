import csv

file= r"C:\Users\KIIT0001\Desktop\MACHINE LEARNING\collection techniques\data.csv"

with open(file,"r") as f:
    read=csv.DictReader(f)
    rows=list(read)

print("Collected Data:")
for row in rows:
 print(row)
 
 print("\nTotal students:", len(rows))