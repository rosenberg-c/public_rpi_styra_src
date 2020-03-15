"""
This file is called from systemd service
"""
import time

from handle_socket import HandleSocket
from tools_lib.lib.time_delta.between_hours import get_date_now, within_timedelta


def _flip(val):
    val ^= True
    return val


def _while_did_press(on_active, pin, handler: HandleSocket, cycle_t):
    if on_active:
        handler.handle_socket(auto_on=True, auto_off=True)
        while on_active:
            did_use = pin.is_on()
            on_active = _flip(did_use)
            if did_use:
                handler.handle_socket(auto_on=True, auto_off=True)
            if get_date_now() > cycle_t:
                on_active = False
            time.sleep(0.1)


def _on_flip_state(on_active, pin, handler: HandleSocket):
    if on_active:
        handler.handle_socket(auto_on=True, auto_off=True)
        while pin.is_on():
            time.sleep(0.1)


def use_gpio(pin1, pin2, handle_screen, next_update):
    _while_did_press(
        on_active=pin1.is_on(),
        pin=pin1,
        handler=handle_screen,
        cycle_t=next_update
    )

    flip_state = pin2.is_on()
    if flip_state:
        _on_flip_state(
            on_active=pin2.is_on(),
            pin=pin2,
            handler=handle_screen
        )
        # return _within_delta(
        #     disable_from=disable_from,
        #     enable_from=enable_from,
        #     auto_on=True,
        #     auto_off=True
        # )
    return False
    ##handle_screen.handle_screen(auto_on=auto_on, auto_off=auto_off)


def off_outside_delta(disable_from, enable_from, auto_off, get_now=None):
    _get_now = get_now or get_date_now

    _within_timedelta = within_timedelta(date_now=_get_now(), delta_begin=disable_from, delta_end=enable_from)

    if auto_off:
        if _within_timedelta:
            return True
    return False


def on_within_delta(disable_from, enable_from, auto_on, get_now=None):
    _get_now = get_now or get_date_now

    _within_timedelta = within_timedelta(date_now=_get_now(), delta_begin=disable_from, delta_end=enable_from)

    if auto_on:
        if _within_timedelta is False:
            return True

    return False


def main_on_off_wrapper(disable_from, enable_from, auto_on, auto_off, handle_socket, get_now=None):
    if off_outside_delta(
            auto_off=auto_off,
            disable_from=disable_from,
            enable_from=enable_from,
            get_now=get_now,
    ):
        print("OFF")
        handle_socket.off(1)

    if on_within_delta(
            auto_on=auto_on,
            disable_from=disable_from,
            enable_from=enable_from,
            get_now=get_now,
    ):
        print("ON")
        handle_socket.on(1)
    print("EOF")
