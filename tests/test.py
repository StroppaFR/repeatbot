from repeatbot import KeyboardRecorder, MouseRecorder, EventsImporter, EventsExporter, Repeater
import time

# Record events
mouseRecorder = MouseRecorder()
keyboardRecorder = KeyboardRecorder()

mouseRecorder.start()
keyboardRecorder.start()
print("Started recording")

time.sleep(10)

mouseRecorder.stop()
keyboardRecorder.stop()
print("Stopped recording")

# Export and import recorded events
EventsExporter.exportEvents(keyboardRecorder.events, "keyboard.csv")
EventsExporter.exportEvents(mouseRecorder.events, "mouse.csv")
events = EventsImporter.importEvents("keyboard.csv")
events.extend(EventsImporter.importEvents("mouse.csv"))

# Repeat events
print("Repeating events")
repeater = Repeater()
repeater.repeatEvents(events)
print("Done")
