from iskedyul.lines import Cell, Line
from iskedyul.models import Days
from iskedyul.scale import TimeScale


class DayGroup:
    def __init__(self, scale, day, events) -> None:
        self.scale = scale
        self.day = day
        self.events = events
        # run the simulation
        self.execute()

    def __findline(self, event, lines):
        index = None
        for i, line in enumerate(lines):
            if line.fit(event):
                index = i
                break
        return index

    def __putevent(self, event, lines):
        lineindex = self.__findline(event, lines)
        if lineindex is not None:
            lines[lineindex].put(event)
        else:
            newline = Line(self.scale)
            newline.put(event)
            lines.append(newline)

    def execute(self):
        lines = [Line(self.scale)]
        for event in self.events:
            self.__putevent(event, lines)

        # store the lines
        self.lines = lines

        # set the head
        head = {}
        head["day"] = self.day
        head["colspan"] = len(lines)
        self.head = head


def getrow(interval, lines):
    row = []
    for line in lines:
        if interval in line.cells:
            cell = line.cells[interval]
        row.append(cell)
    return row


def getrows(scale, lines):
    rows = {}
    for interval in scale.intervals:
        rows[interval] = getrow(interval, lines)
    return rows


class TimetableViewer:
    def __init__(self, events, scale=TimeScale(30, 7, 20)) -> None:
        self.scale = scale
        self.init_daygroups(events)

    def init_daygroups(self, events):
        events_by_day = events.group_by_days(Days.values)

        daygroups = []
        for d, qset in events_by_day.items():
            daygroups.append(DayGroup(self.scale, Days(d), qset))

        self.daygroups = daygroups

    @property
    def head(self):
        heads = []
        for dg in self.daygroups:
            head = dg.head
            heads.append(head)
        return heads

    @property
    def body(self):
        lines = []
        for dg in self.daygroups:
            dglines = dg.lines
            lines.extend(dglines)
        rows = getrows(self.scale, lines)

        return rows
