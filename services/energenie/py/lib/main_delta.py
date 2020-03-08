from tools_lib.lib.time_delta.between_hours import within_timedelta, get_date_now


def within_delta(disable_from, enable_from, auto_on, auto_off, date_now=None):
    _date_now = date_now or get_date_now()
    _within_timedelta = within_timedelta(date_now=_date_now, delta_begin=disable_from, delta_end=enable_from)
    
    if auto_on:
        if _within_timedelta is False:
            print("outside delta")
            return True

    if auto_off:
        if _within_timedelta:
            print("within delta")
            return False
    return False
