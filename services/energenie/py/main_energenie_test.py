import unittest

from lib.main_delta import within_delta
from tools_lib.lib.time_delta.between_hours import get_date_now


class TestStringMethods(unittest.TestCase):
    def test2(self):
        self.assertTrue(
            within_delta(
                date_now=get_date_now(str_now="01:59:00"),
                disable_from="01:00:00",
                enable_from="02:00:00",
                auto_on=True,
                auto_off=True,
                # date_now=get_date_now(str_now="01:59:00"),
                # disable_from="01:00:00",
                # enable_from="02:00:00",
            )
        )

    def test5(self):
        self.assertTrue(
            within_delta(
                date_now=get_date_now(str_now="01:59:00"),
                disable_from="23:00:00",
                enable_from="02:00:00",
                auto_on=True,
                auto_off=True,
            )
        )

    def test6(self):
        self.assertTrue(
            within_delta(
                date_now=get_date_now(str_now="01:59:00"),
                disable_from="23:00:00",
                enable_from="02:00:00",
                auto_on=True,
                auto_off=True,
            )
        )

    def test4(self):
        self.assertFalse(
            within_delta(
                date_now=get_date_now(str_now="22:00:00"),
                disable_from="23:00:00",
                enable_from="02:00:00",
                auto_on=True,
                auto_off=True,
            )
        )

    def test7(self):
        self.assertFalse(
            within_delta(
                date_now=get_date_now(str_now="02:02:00"),
                disable_from="23:00:00",
                enable_from="02:00:00",
                auto_on=True,
                auto_off=True,
            )
        )

    def test3(self):
        self.assertFalse(
            within_delta(
                date_now=get_date_now(str_now="03:59:00"),
                disable_from="01:00:00",
                enable_from="02:00:00",
                auto_on=True,
                auto_off=True,
            )
        )

    def test9(self):
        self.assertFalse(
            within_delta(
                date_now=get_date_now(str_now="00:00:01"),
                disable_from="00:00:00",
                enable_from="00:00:00",
                auto_on=True,
                auto_off=True,
            )
        )

    def test1(self):
        self.assertFalse(
            within_delta(
                date_now=get_date_now(str_now="00:59:00"),
                disable_from="01:00:00",
                enable_from="02:00:00",
                auto_on=True,
                auto_off=True,
            )
        )

    def test8(self):
        self.assertFalse(
            within_delta(
                date_now=get_date_now(str_now="00:00:00"),
                disable_from="00:00:00",
                enable_from="00:00:00",
                auto_on=True,
                auto_off=True,
            )
        )
