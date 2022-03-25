import pynput
from datetime import datetime

class KeyboardRecorder:
    def __init__(self):
        self.recordPress = True
        self.recordRelease = True
        self.listener = None
        self.events = []

    def on_press(self, key):
        t = datetime.now()
        print(t, key)

    def on_release(self, key):
        t = datetime.now()
        print(t, key)

    def start(self):
        self.listener = pynput.keyboard.Listener(
                on_press=self.on_press if self.recordPress else None,
                on_release=self.on_release if self.recordRelease else None)
        self.listener.start()

    def stop(self):
        self.listener.stop()

class MouseRecorder:
    def __init__(self):
        self.recordMove = True
        self.recordClick = True
        self.recordScroll = True
        self.listener = None
        self.events = []

    def on_move(self, x, y):
        t = datetime.now()
        print(t, x, y)

    def on_click(self, x, y, button, pressed):
        t = datetime.now()
        print(t, x, y, button, pressed)

    def on_scroll(self, x, y, dx, dy):
        t = datetime.now()
        print(t, x, y, dx, dy)

    def start(self):
        self.listener = pynput.mouse.Listener(
                on_move=self.on_move if self.recordMove else None,
                on_click=self.on_click if self.recordClick else None,
                on_scroll=self.on_scroll if self.recordScroll else None)
        self.listener.start()

    def stop(self):
        self.listener.stop()
