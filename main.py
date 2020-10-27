class Interviewer:
    def __init__(self, work_start, work_end):
        self.work_start = work_start
        self.work_end = work_end
        self.booked_events = []

    def book(self, start, duration):
        event = Event(start, duration)
        end = event.end()
        assert start.time() > self.work_start, "Requested event starts too early"
        assert end.time() < self.work_end, "Requested event runs until too late"
        for existing_event in self.booked_events:
            assert end < existing_event.start or existing_event.end() < start, \
                "Requested event overlaps with existing event"
        self.booked_events.append(event)


class Event:
    def __init__(self, start, duration):
        self.start = start
        self.duration = duration

    def end(self):
        return self.start + self.duration
