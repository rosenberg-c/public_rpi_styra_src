import unittest
from .between_hours import within_timedelta, get_date_now


class TestStringMethods(unittest.TestCase):
    def test2(self):
        self.assertTrue(
            within_timedelta(
                date_now=get_date_now(str_now="01:59:00"),
                delta_begin="01:00:00",
                delta_end="02:00:00",
            )
        )

    def test5(self):
        self.assertTrue(
            within_timedelta(
                date_now=get_date_now(str_now="23:01:00"),
                delta_begin="23:00:00",
                delta_end="02:00:00",
            )
        )

    def test6(self):
        self.assertTrue(
            within_timedelta(
                date_now=get_date_now(str_now="01:59:00"),
                delta_begin="23:00:00",
                delta_end="02:00:00",
            )
        )

    def test4(self):
        self.assertFalse(
            within_timedelta(
                date_now=get_date_now(str_now="22:00:00"),
                delta_begin="23:00:00",
                delta_end="02:00:00",
            )
        )

    def test7(self):
        self.assertFalse(
            within_timedelta(
                date_now=get_date_now(str_now="02:02:00"),
                delta_begin="23:00:00",
                delta_end="02:00:00",
            )
        )

    def test3(self):
        self.assertFalse(
            within_timedelta(
                date_now=get_date_now(str_now="03:59:00"),
                delta_begin="01:00:00",
                delta_end="02:00:00",
            )
        )

    def test9(self):
        self.assertFalse(
            within_timedelta(
                date_now=get_date_now(str_now="00:00:01"),
                delta_begin="00:00:00",
                delta_end="00:00:00",
            )
        )

    def test1(self):
        self.assertFalse(
            within_timedelta(
                date_now=get_date_now(str_now="00:59:00"),
                delta_begin="01:00:00",
                delta_end="02:00:00",
            )
        )

    def test8(self):
        self.assertFalse(
            within_timedelta(
                date_now=get_date_now(str_now="00:00:00"),
                delta_begin="00:00:00",
                delta_end="00:00:00",
            )
        )
