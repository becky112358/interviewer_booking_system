import datetime
import unittest

from main import Interviewer


class InterviewerTests(unittest.TestCase):
    def test_successfully_add_meetings(self):
        """
        Create two interviewers.
        Book some interviews with the interviewers.
        All booked interviews should be successfully booked.
        """
        andy = Interviewer(work_start=datetime.time(hour=8, minute=0, second=0),
                           work_end=datetime.time(hour=16, minute=0, second=0))
        brook = Interviewer(work_start=datetime.time(hour=10, minute=0, second=0),
                            work_end=datetime.time(hour=18, minute=35, second=0))
        andy.book(datetime.datetime(year=2020, month=3, day=14, hour=10, minute=0, second=0),
                  datetime.timedelta(seconds=3599))
        brook.book(datetime.datetime(year=2020, month=3, day=14, hour=10, minute=0, second=0),
                   datetime.timedelta(seconds=3599))
        andy.book(datetime.datetime(year=2020, month=3, day=14, hour=11, minute=0, second=0),
                  datetime.timedelta(seconds=1800))
        andy.book(datetime.datetime(year=2020, month=3, day=14, hour=15, minute=9, second=26),
                  datetime.timedelta(seconds=1))
        brook.book(datetime.datetime(year=2020, month=2, day=7, hour=18, minute=28, second=18),
                   datetime.timedelta(seconds=28))
        # Book an interview to be at the same time of day as an already booked interview,
        # but on a different day.
        andy.book(datetime.datetime(year=2020, month=3, day=1, hour=10, minute=0, second=0),
                  datetime.timedelta(seconds=3599))
        self.assertEqual(len(andy.booked_events), 4)
        self.assertEqual(len(brook.booked_events), 2)

    def test_meeting_too_early(self):
        cameron = Interviewer(work_start=datetime.time(hour=9, minute=15, second=0),
                              work_end=datetime.time(hour=17, minute=45, second=0))
        with self.assertRaises(AssertionError):
            cameron.book(datetime.datetime(year=2000, month=1, day=2, hour=3, minute=4, second=5),
                         datetime.timedelta(seconds=12345))
        self.assertEqual(len(cameron.booked_events), 0)
