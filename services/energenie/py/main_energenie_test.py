import unittest
from datetime import timedelta
from unittest import mock

from handle_socket import HandleSocket
from lib.get_energenie_config import EnergenieConfig
from main_function import main_on_off_wrapper
from tools_lib.lib.time_delta.between_hours import get_date_now


class TestStringMethods(unittest.TestCase):
    def test_screen_1_a(self):
        energenie_config = EnergenieConfig(
            auto_on=False,
            auto_off=False,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="23:59:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now
        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    def test_screen_1_b(self):
        energenie_config = EnergenieConfig(
            auto_on=False,
            auto_off=False,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:00:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    def test_screen_1_c(self):
        energenie_config = EnergenieConfig(
            auto_on=False,
            auto_off=False,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:01:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    # AUTO ON
    def test_screen_2_a(self):
        energenie_config = EnergenieConfig(
            auto_on=True,
            auto_off=False,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="23:59:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    def test_screen_2_b(self):
        energenie_config = EnergenieConfig(
            auto_on=True,
            auto_off=False,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:00:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_called()
        mock_off.assert_not_called()

    def test_screen_2_c(self):
        energenie_config = EnergenieConfig(
            auto_on=True,
            auto_off=False,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:01:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    # AUTO ON OFF
    def test_screen_3_a(self):
        energenie_config = EnergenieConfig(
            auto_on=True,
            auto_off=True,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="23:59:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_called()

    def test_screen_3_b(self):
        energenie_config = EnergenieConfig(
            auto_on=True,
            auto_off=True,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:00:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_called()
        mock_off.assert_not_called()

    def test_screen_3_c(self):
        energenie_config = EnergenieConfig(
            auto_on=True,
            auto_off=True,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:01:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_called()

    # AUTO OFF
    def test_screen_4_a(self):
        energenie_config = EnergenieConfig(
            auto_on=False,
            auto_off=True,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="23:59:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_called()

    def test_screen_4_b(self):
        energenie_config = EnergenieConfig(
            auto_on=False,
            auto_off=True,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:00:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_not_called()

    def test_screen_4_c(self):
        energenie_config = EnergenieConfig(
            auto_on=False,
            auto_off=True,
            enable_from="00:00:00",
            disable_from="00:01:00",
            update_cycle=6,
            ignore_gpio=True,
            name="test"
        )
        now = get_date_now(str_now="00:01:30")
        next_update = now + timedelta(seconds=energenie_config.update_cycle)

        mock_on = mock.Mock(return_value="mocked stuff")
        mock_off = mock.Mock(return_value="mocked stuff")
        mock_date_now = mock.Mock(return_value=now)
        main_on_off_wrapper(
            enable_from=energenie_config.enable_from,
            disable_from=energenie_config.disable_from,
            auto_on=energenie_config.auto_on,
            auto_off=energenie_config.auto_off,
            handle_socket=HandleSocket(on=mock_on, off=mock_off),
            get_now=mock_date_now

        )
        mock_on.assert_not_called()
        mock_off.assert_called()
