from datetime import datetime, timedelta

YMD_format = '%Y-%m-%d'
HMS_format = '%H:%M:%S'


def date_from_str(str_date: str, str_hours: str, t_format: str = YMD_format + 'T' + HMS_format) -> datetime:
    return datetime.strptime(str_date + 'T' + str_hours, t_format)


def get_date_now(str_date: str = None, str_now: str = None) -> datetime:
    # Ensure current date
    str_date = str_date or datetime.now().date().strftime(YMD_format)
    str_now = str_now or datetime.now().time().strftime(HMS_format)

    dt: datetime = date_from_str(str_date, str_now)
    return datetime(
        year=dt.year, month=dt.month, day=dt.day,
        hour=dt.hour, minute=dt.minute, second=dt.second
    )


def date(time: datetime, is_before: datetime) -> bool:
    return time < is_before


def now_is_between_start_and_end(now, start, end):
    if date(time=start, is_before=now):
        if date(time=now, is_before=end):
            return True
    return False


def now_is_between_start_and_next_end(now, start, end, next_end):
    if date(time=start, is_before=now):
        if date(time=end, is_before=start):
            if date(time=start, is_before=now):
                if date(time=now, is_before=next_end):
                    return True
    return False


def next_now_is_between_start_and_next_end(now, next_now, start, end, next_end):
    if date(time=now, is_before=end):
        if date(time=now, is_before=start):
            if date(time=end, is_before=start):
                if date(time=start, is_before=next_now):
                    if date(time=next_now, is_before=next_end):
                        return True
    return False


def now_between(now: datetime, start: datetime, end: datetime) -> bool:
    next_end = end + timedelta(days=1)
    next_now = now + timedelta(days=1)

    if now_is_between_start_and_end(now, start, end):
        return True
    if now_is_between_start_and_next_end(now, start, end, next_end):
        return True
    if next_now_is_between_start_and_next_end(now, next_now, start, end, next_end):
        return True
    return False


def within_timedelta(date_now=get_date_now(), delta_begin="00:00:00", delta_end="00:00:00") -> bool:
    dt_time_start = datetime.strptime(delta_begin, HMS_format).time()
    dt_time_end = datetime.strptime(delta_end, HMS_format).time()

    if now_between(
            now=date_now,
            start=date_now.replace(
                hour=dt_time_start.hour,
                minute=dt_time_start.minute,
                second=dt_time_start.second
            ),
            end=date_now.replace(
                hour=dt_time_end.hour,
                minute=dt_time_end.minute,
                second=dt_time_end.second
            )):
        return True
    return False
