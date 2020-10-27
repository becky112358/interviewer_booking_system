class Interviewer:
    """
    Current assumptions:
    - An interviewer has worked since the beginning of time, and will work until the end of time
    - An interviewer works every day of the week
    - An interviewer finishes their working day on the same day that they start their working day
      (ie an interviewer does not work past midnight)
    - An interviewer does not take unbooked breaks throughout the day
    - Interviews can be booked in the past as well as the future

    :param work_start: datetime.time , time at which the interviewer starts work
    :param work_end: datetime.time , time at which the interviewer ends work
    """
    def __init__(self, work_start, work_end):
        self.work_start = work_start
        self.work_end = work_end
        self.booked_events = []

    def book(self, start, duration):
        """
        An interview can be attempted to be booked with the interview.
        To be successfully booked, it must:
        - take place during the working time of the interviewer
        - not overlap with existing interviews

        :param start: datetime.datetime
        :param duration: datetime.timedelta
        """
        event = Event(start, duration)
        end = event.end()
        assert start.time() >= self.work_start, "Requested event starts too early"
        assert end.time() <= self.work_end, "Requested event runs until too late"
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
