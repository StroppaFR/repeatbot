from repeatbot.recorder import KeyboardRecorder, MouseRecorder
from repeatbot.common import Event
import time
import csv

mouseRecorder = MouseRecorder()
keyboardRecorder = KeyboardRecorder()
mouseRecorder.start()
keyboardRecorder.start()
print("Started")
time.sleep(3)
mouseRecorder.stop()
keyboardRecorder.stop()
print("Stopped")
keyboardRecorder.saveEvents('out.csv')

with open('out.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        e = Event.fromCsvRow(row)
    
