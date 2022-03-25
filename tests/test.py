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

# Export and Import recorded keyboard events
EventsExporter.exportEvents(keyboardRecorder.events, "events.csv")
events = EventsImporter.importEvents("events.csv")

# Repeat keyboard events
print("Repeating events")
repeater = Repeater()
repeater.repeatEvents(events)
print("Done")
