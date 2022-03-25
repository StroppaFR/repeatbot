from datetime import datetime
from enum import Enum
from pynput.keyboard import Key, KeyCode

class EventKind(Enum):
    KEY_PRESS = 0
    KEY_RELEASE = 1
    MOUSE_MOVE = 2
    MOUSE_PRESS = 3
    MOUSE_RELEASE = 4
    MOUSE_SCROLL = 5

class EventParamType(Enum):
    KEY = 0
    KEYCODE_CHAR = 1
    KEYCODE_VK = 2

class Event:
    def __init__(self, time, kind, data):
        self.time = time
        self.kind = kind
        self.data = data

    def normalize(self, t0):
        self.time = self.time - t0

    def asCsvRow(self):
        row = [datetime.timestamp(self.time), self.kind.name]
        for d in self.data:
            if type(d) is Key:
                row.append(EventParamType.KEY.name)
                row.append(d.name)
            elif type(d) is KeyCode:
                if d.char is not None:
                    row.append(EventParamType.KEYCODE_CHAR.name)
                    row.append(d.char)
                elif d.vk is not None:
                    row.append(EventParamType.KEYCODE_VK.name)
                    row.append(d.vk)
        return row
    
    @staticmethod
    def fromCsvRow(row):
        time = datetime.fromtimestamp(float(row[0]))
        kind = EventKind[row[1]]
        if kind in [EventKind.KEY_PRESS, EventKind.KEY_RELEASE]:
            paramType = EventParamType[row[2]]
            param = row[3]
            if paramType == EventParamType.KEY:
                data = [Key[param]]
            elif paramType == EventParamType.KEYCODE_CHAR:
                data = [KeyCode.from_char(param)]
            elif paramType == EventParamType.KEYCODE_VK:
                data = [KeyCode.from_vk(int(param))]
        return Event(time, kind, data)
