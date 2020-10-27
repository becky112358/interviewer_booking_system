import datetime


class Interviewer:
    def __init__(self, work_start, work_end):
        self.work_start = work_start
        self.work_end = work_end
        self.booked_events = []

    def book(self, start, duration):
        add_event = True
        event = Event(start, duration)
        end = event.end()
        if start.time() < self.work_start:
            add_event = False
            print("Requested event starts too early")
        elif end.time() > self.work_end:
            add_event = False
            print("Requested event runs until too late")
        else:
            for existing_event in self.booked_events:
                if (start < existing_event.start < end) \
                        or (existing_event.start < start < existing_event.end()):
                    print("Requested event overlaps with existing event")
                    add_event = False

        if add_event:
            self.booked_events.append(event)


class Event:
    def __init__(self, start, duration):
        self.start = start
        self.duration = duration

    def end(self):
        return self.start + self.duration


bob_workstart = datetime.time(hour=8, minute=0, second=0)
bob_workend = datetime.time(hour=16, minute=0, second=0)
bob = Interviewer(work_start=bob_workstart, work_end=bob_workend)
bob.book(datetime.datetime(year=2020, month=10, day=27, hour=10, minute=0, second=0),
         datetime.timedelta(seconds=3600))
bob.book(datetime.datetime(year=2020, month=10, day=27, hour=10, minute=1, second=0),
         datetime.timedelta(seconds=20))
