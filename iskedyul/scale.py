from datetime import time


class TimeInterval:
    def __init__(self, h1, m1, h2, m2):
        self.start = time(h1, m1)
        self.end = time(h2, m2)

    def __repr__(self) -> str:
        return repr((self.start, self.end))

    def __eq__(self, other):
        if isinstance(other, TimeInterval):
            return (self.start, self.end) == (other.start, other.end)
        return False

    def __hash__(self):
        return hash((self.start, self.end))


class TimeScale:
    def __init__(self, interval, start_hour, end_hour) -> None:
        self.interval = interval
        self.start_hour = start_hour
        self.end_hour = end_hour

    @property
    def intervals(self):
        interval_minutes = self.interval
        start_hour = self.start_hour
        end_hour = self.end_hour
        # Initialize the list to store the Time objects
        time_intervals = []

        # Generate a list of hours within the specified range
        hours_range = range(start_hour, end_hour + 1)

        # Calculate the valid multiples of the interval within [0, 59]
        valid_multiples = set(range(0, 60, interval_minutes))

        # Generate time intervals as Time objects
        for hour in hours_range:
            for minute in valid_multiples:
                h1 = hour
                m1 = minute
                minutes_lt_60 = minute + interval_minutes < 60
                if minutes_lt_60:
                    h2 = hour
                    m2 = minute + interval_minutes
                else:
                    h2 = hour + 1
                    m2 = 0
                hour_lt_end_hour = hour < end_hour
                hour_eq_end_hour = hour == end_hour
                if hour_lt_end_hour or hour_eq_end_hour and minutes_lt_60:
                    time_intervals.append(TimeInterval(h1, m1, h2, m2))

        return time_intervals

    def event_intervals(self, event):
        intervals = []
        event_start = event.start_time
        event_end = event.end_time
        # Iterate through the generated time intervals
        # and check if the event's start and end times fall within them
        for interval in self.intervals:
            if event_start <= interval.start and event_end >= interval.end:
                intervals.append(interval)

        return intervals
