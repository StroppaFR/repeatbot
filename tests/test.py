from repeatbot.recorder import KeyboardRecorder, MouseRecorder
import time

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
