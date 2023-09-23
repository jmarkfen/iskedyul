from iskedyul.scale import TimeScale

class Cell(dict):
    def __init__(self, event=None, **attrs):
        if event is not None:
            self["event"] = event
        self.update(attrs)

    def empty(self):
        return "event" not in self


class Line(dict):
    def __init__(self, scale: TimeScale, initial=0) -> None:
        self.scale = scale
        self.initial = initial
        for interval in scale.intervals:
            self[interval] = initial

    @property
    def cells(self):
        cells = {}
        for key, val in self.items():
            if val == self.initial:
                cell = Cell()
            elif isinstance(val, Cell):
                cell = val
            elif val is None:
                cell = None
            cells[key] = cell
        return cells

    def fit(self, event):
        result = []
        intervals = self.scale.event_intervals(event)

        for i in intervals:
            isinitial = i in self and self[i] == self.initial
            result.append(isinitial)

        return all(result)

    def put(self, event):
        intervals = self.scale.event_intervals(event)
        first = intervals[0]
        self[first] = Cell(event, rowspan=len(intervals))
        for i in range(1, len(intervals)):
            key = intervals[i]
            self[key] = None

