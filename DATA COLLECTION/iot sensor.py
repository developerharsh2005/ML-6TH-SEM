import serial
import csv

ser = serial.Serial('COM3', 9600)  # Your Arduino port

with open("sensor_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Reading"])

    for i in range(10):  
        value = ser.readline().decode().strip()
        writer.writerow([value])
        print(value)
