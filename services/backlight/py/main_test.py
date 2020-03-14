import unittest
from datetime import timedelta
from unittest import mock

from lib.get_backlight_config import BacklightConfig
from main_function import HandleScreen, main_on_off_wrapper
from tools_lib.lib.time_delta.between_hours import get_date_now


class Test(unittest.TestCase):
    # AUTO OFF
    def test_screen_1_a(self):
        backlight_config = BacklightConfig(
            auto_on=False,
            auto_off=False,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="23:59:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    def test_screen_1_b(self):
        backlight_config = BacklightConfig(
            auto_on=False,
            auto_off=False,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:00:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    def test_screen_1_c(self):
        backlight_config = BacklightConfig(
            auto_on=False,
            auto_off=False,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:01:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    # AUTO ON
    def test_screen_2_a(self):
        backlight_config = BacklightConfig(
            auto_on=True,
            auto_off=False,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="23:59:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_called()
        mock_off.assert_not_called()

    def test_screen_2_b(self):
        backlight_config = BacklightConfig(
            auto_on=True,
            auto_off=False,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:00:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    def test_screen_2_c(self):
        backlight_config = BacklightConfig(
            auto_on=True,
            auto_off=False,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:01:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_called()
        mock_off.assert_not_called()

    # AUTO ON OFF
    def test_screen_3_a(self):
        backlight_config = BacklightConfig(
            auto_on=True,
            auto_off=True,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="23:59:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_called()
        mock_off.assert_not_called()

    def test_screen_3_b(self):
        backlight_config = BacklightConfig(
            auto_on=True,
            auto_off=True,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:00:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_called()

    def test_screen_3_c(self):
        backlight_config = BacklightConfig(
            auto_on=True,
            auto_off=True,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:01:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_called()
        mock_off.assert_not_called()

    # AUTO OFF
    def test_screen_4_a(self):
        backlight_config = BacklightConfig(
            auto_on=False,
            auto_off=True,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="23:59:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    def test_screen_4_b(self):
        backlight_config = BacklightConfig(
            auto_on=False,
            auto_off=True,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:00:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_called()

    def test_screen_4_c(self):
        backlight_config = BacklightConfig(
            auto_on=False,
            auto_off=True,
            disable_from="00:00:00",
            enable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:01:30")
        next_update = now + timedelta(seconds=backlight_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            disable_from=backlight_config.disable_from,
            enable_from=backlight_config.enable_from,
            auto_on=backlight_config.auto_on,
            auto_off=backlight_config.auto_off,
            handle_screen=HandleScreen(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()
