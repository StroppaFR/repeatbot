import pynput
import csv
from datetime import datetime
from .common import Event, EventKind

class KeyboardRecorder:
    def __init__(self):
        self.recordPress = True
        self.recordRelease = True
        self.listener = None
        self.events = []

    def on_press(self, key):
        self.events.append(Event(datetime.now(), EventKind.KEY_PRESS, [key]))

    def on_release(self, key):
        self.events.append(Event(datetime.now(), EventKind.KEY_RELEASE, [key]))

    def start(self):
        self.listener = pynput.keyboard.Listener(
                on_press=self.on_press if self.recordPress else None,
                on_release=self.on_release if self.recordRelease else None)
        self.listener.start()

    def stop(self):
        self.listener.stop()

    def saveEvents(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for event in self.events:
                writer.writerow(event.asCsvRow())

class MouseRecorder:
    def __init__(self):
        self.recordMove = True
        self.recordClick = True
        self.recordScroll = True
        self.listener = None
        self.events = []

    def on_move(self, x, y):
       self.events.append(Event(datetime.now(), EventKind.MOUSE_MOVE, [x, y]))

    def on_click(self, x, y, button, pressed):
        self.events.append(Event(datetime.now(), EventKind.MOUSE_MOVE, [x, y, button, pressed]))

    def on_scroll(self, x, y, dx, dy):
        self.events.append(Event(datetime.now(), EventKind.MOUSE_MOVE, [x, y, dx, dy]))

    def start(self):
        self.listener = pynput.mouse.Listener(
                on_move=self.on_move if self.recordMove else None,
                on_click=self.on_click if self.recordClick else None,
                on_scroll=self.on_scroll if self.recordScroll else None)
        self.listener.start()

    def stop(self):
        self.listener.stop()
