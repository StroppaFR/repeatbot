from repeatbot.recorder import KeyboardRecorder, MouseRecorder
import time

mouseRecorder = MouseRecorder()
keybardRecorder = KeyboardRecorder()
mouseRecorder.start()
keybardRecorder.start()
print("Started")
time.sleep(3)
mouseRecorder.stop()
keybardRecorder.stop()
print("Stopped")
time.sleep(3)
