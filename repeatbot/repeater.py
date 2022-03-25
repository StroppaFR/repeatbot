import pynput
from datetime import datetime
from .common import Event, EventKind

class Repeater:
    def __init__(self):
        self.keyboard = pynput.keyboard.Controller()
        self.mouse = pynput.mouse.Controller()

    def repeatEvents(self, events, normalize=False):
        if events == []:
            return
        events = sorted(events, key=lambda event: event.time)
        if normalize:
            for event in events:
                event.normalize(events[0].time)
        t0 = datetime.now()
        while events != []:
            if datetime.now() - t0 >= events[0].time:
                event = events.pop(0)
                if event.kind == EventKind.KEY_PRESS:
                    key = event.data[0]
                    self.keyboard.press(key)
                elif event.kind == EventKind.KEY_RELEASE:
                    key = event.data[0]
                    self.keyboard.release(key)
