import sys

sys.path.append("lib")

import serial
import time

ser = serial.Serial('COM5', 9600, timeout=1)

ser.write(b'1')

time.sleep(3)

ser.write(b'5')
