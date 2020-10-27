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
        if start < self.work_start:
            add_event = False
            print("Requested event starts too early")
        elif end > self.work_end:
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
        duration_hours = self.duration // 60
        duration_minutes = (self.duration % 3600 - self.duration % 60) / 60
        duration_seconds = self.duration % 60

        return datetime.time(hour=self.start.hour, # + duration_hours,
                             minute=self.start.minute, #+ duration_minutes,
                             second=self.start.second) #+ duration_seconds)


bob_workstart = datetime.time(hour=8, minute=0, second=0)
bob_workend = datetime.time(hour=16, minute=0, second=0)
bob = Interviewer(work_start=bob_workstart, work_end=bob_workend)
bob.book(datetime.time(hour=10, minute=0, second=0), 3600)

t = datetime.timedelta(seconds=589)
print(t)
t.
t1 = datetime.time(hour=5, minute=3, second=8)
print(t1)
t2 = datetime.time(hour=t1.hour + t.hour, minute=t1.hour + t.hours)
