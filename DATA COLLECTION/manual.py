import csv

data = [
    ["Date", "Name", "Status"],
    ["2025-02-01", "Rahul", "Present"],
    ["2025-02-01", "Isha", "Absent"]
]

with open("attendance.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("attendance.csv created")
