import serial
import csv
from time import sleep

device = serial.Serial('COM4', 115200, timeout=1)
address_loc = "Function Tests/addresser.csv"

with open(address_loc, newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')

    for row in reader:
        print(row)
        sleep(.500)






device.write(b'H')


