import csv

# Create CSV file with header
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])

    
    for i in range(5):
       
        Name = input("Enter name: ")
        age = input("Enter age: ")
        city = input("Enter city: ")

        writer.writerow([Name, age, city])

print("\nAll 5 entries saved to data.csv!")