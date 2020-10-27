import datetime
import unittest

from main import Interviewer


class InterviewerTests(unittest.TestCase):
    def test_successfully_add_meetings(self):
        """
        Create an interviewer.
        Book some interviews with the interviewer.
        All booked interviews should be successfully booked.
        """
        andy_work_start = datetime.time(hour=8, minute=0, second=0)
        andy_work_end = datetime.time(hour=16, minute=0, second=0)
        andy = Interviewer(work_start=andy_work_start, work_end=andy_work_end)
        andy.book(datetime.datetime(year=2020, month=3, day=14, hour=10, minute=0, second=0),
                  datetime.timedelta(seconds=3599))
        andy.book(datetime.datetime(year=2020, month=3, day=14, hour=11, minute=0, second=0),
                  datetime.timedelta(seconds=1800))
        andy.book(datetime.datetime(year=2020, month=3, day=14, hour=15, minute=9, second=26),
                  datetime.timedelta(seconds=1))
        # Book an interview to be at the same time of day as an already booked interview,
        # but on a different day.
        andy.book(datetime.datetime(year=2020, month=3, day=1, hour=10, minute=0, second=0),
                  datetime.timedelta(seconds=3599))
        self.assertEqual(len(andy.booked_events), 4)
