from datetime import datetime, timedelta

import humanize


def relative_time(date: datetime) -> str:
    """
    Returns a humanized string representing time difference
    between now() and the input datetime object

    eg. "2 minutes ago", "in 11 months", "yesterday", etc.
    """
    now = datetime.now()
    # if the second is the same, return "now"
    if now.strftime("%Y%m%d%H%M%S") == date.strftime("%Y%m%d%H%M%S"):
        return "now"
    # get the time difference between now() and the input datetime object
    delta = date - now
    abs_time_delta = now - (now + delta) if delta.days < 0 else delta
    abs_time_delta += timedelta(seconds=1)  # add 1 second to avoid rounding errors
    delta_days = abs_time_delta.days
    delta_seconds = abs_time_delta.seconds
    if delta_days >= 365:
        num_years = round(delta_days / 365)
        result = "a year" if num_years == 1 else f"{num_years} years"
    elif delta_days >= 30:
        num_months = round(delta_days / 30)
        result = "a month" if num_months == 1 else f"{num_months} months"
    elif delta_days >= 7:
        num_weeks = round(delta_days / 7)
        result = "a week" if num_weeks == 1 else f"{num_weeks} weeks"
    elif delta_days >= 1:
        result = "a day" if delta_days == 1 else f"{delta_days} days"
    elif delta_seconds >= 3600:
        num_hours = round(delta_seconds / 3600)
        result = "an hour" if num_hours == 1 else f"{num_hours} hours"
    elif delta_seconds >= 60:
        num_minutes = round(delta_seconds / 60)
        result = "a minute" if num_minutes == 1 else f"{num_minutes} minutes"
    else:
        result = "a few seconds"
    # if the input datetime object is in the future, return "in X", otherwise "X ago"
    return f"in {result}" if date > now else f"{result} ago"


def test_relative_time():
    now = datetime.now()
    in_a_second = now + timedelta(seconds=1)
    in_a_minute = now + timedelta(minutes=1)
    in_an_hour = now + timedelta(hours=1)
    in_a_day = now + timedelta(days=1)
    in_a_week = now + timedelta(weeks=1)
    in_a_month = now + timedelta(days=30)
    in_a_year = now + timedelta(days=365)
    in_40_seconds = now + timedelta(seconds=40)
    in_40_minutes = now + timedelta(minutes=40)
    in_7_hours = now + timedelta(hours=7)
    in_3_days = now + timedelta(days=3)
    in_3_weeks = now + timedelta(weeks=3)
    in_3_months = now + timedelta(days=90)
    in_3_years = now + timedelta(days=365 * 3)
    a_second_ago = now - timedelta(seconds=1)
    a_minute_ago = now - timedelta(minutes=1)
    an_hour_ago = now - timedelta(hours=1)
    a_day_ago = now - timedelta(days=1)
    a_week_ago = now - timedelta(weeks=1)
    a_month_ago = now - timedelta(days=30)
    a_year_ago = now - timedelta(days=365)
    seconds_ago_40 = now - timedelta(seconds=40)
    minutes_ago_40 = now - timedelta(minutes=40)
    hours_ago_7 = now - timedelta(hours=7)
    days_ago_3 = now - timedelta(days=3)
    weeks_ago_3 = now - timedelta(weeks=3)
    months_ago_3 = now - timedelta(days=90)
    years_ago_3 = now - timedelta(days=365 * 3)
    assert (
        relative_time(in_a_second) == "in a few seconds"
    ), f"Expected 'in a few seconds', got {relative_time(in_a_second)}"
    assert (
        relative_time(in_a_minute) == "in a minute"
    ), f"Expected 'in a minute', got {relative_time(in_a_minute)}"
    assert (
        relative_time(in_an_hour) == "in an hour"
    ), f"Expected 'in an hour', got {relative_time(in_an_hour)}"
    assert (
        relative_time(in_a_day) == "in a day"
    ), f"Expected 'in a day', got {relative_time(in_a_day)}"
    assert (
        relative_time(in_a_week) == "in a week"
    ), f"Expected 'in a week', got {relative_time(in_a_week)}"
    assert (
        relative_time(in_a_month) == "in a month"
    ), f"Expected 'in a month', got {relative_time(in_a_month)}"
    assert (
        relative_time(in_a_year) == "in a year"
    ), f"Expected 'in a year', got {relative_time(in_a_year)}"
    assert (
        relative_time(in_40_seconds) == "in a few seconds"
    ), f"Expected 'in a few seconds', got {relative_time(in_40_seconds)}"
    assert (
        relative_time(in_40_minutes) == "in 40 minutes"
    ), f"Expected 'in 40 minutes', got {relative_time(in_40_minutes)}"
    assert (
        relative_time(in_7_hours) == "in 7 hours"
    ), f"Expected 'in 7 hours', got {relative_time(in_7_hours)}"
    assert (
        relative_time(in_3_days) == "in 3 days"
    ), f"Expected 'in 3 days', got {relative_time(in_3_days)}"
    assert (
        relative_time(in_3_weeks) == "in 3 weeks"
    ), f"Expected 'in 3 weeks', got {relative_time(in_3_weeks)}"
    assert (
        relative_time(in_3_months) == "in 3 months"
    ), f"Expected 'in 3 months', got {relative_time(in_3_months)}"
    assert (
        relative_time(in_3_years) == "in 3 years"
    ), f"Expected 'in 3 years', got {relative_time(in_3_years)}"
    assert (
        relative_time(a_second_ago) == "a few seconds ago"
    ), f"Expected 'a few seconds ago', got {relative_time(a_second_ago)}"
    assert (
        relative_time(a_minute_ago) == "a minute ago"
    ), f"Expected 'a minute ago', got {relative_time(a_minute_ago)}"
    assert (
        relative_time(an_hour_ago) == "an hour ago"
    ), f"Expected 'an hour ago', got {relative_time(an_hour_ago)}"
    assert (
        relative_time(a_day_ago) == "a day ago"
    ), f"Expected 'a day ago', got {relative_time(a_day_ago)}"
    assert (
        relative_time(a_week_ago) == "a week ago"
    ), f"Expected 'a week ago', got {relative_time(a_week_ago)}"
    assert (
        relative_time(a_month_ago) == "a month ago"
    ), f"Expected 'a month ago', got {relative_time(a_month_ago)}"
    assert (
        relative_time(a_year_ago) == "a year ago"
    ), f"Expected 'a year ago', got {relative_time(a_year_ago)}"
    assert (
        relative_time(seconds_ago_40) == "a few seconds ago"
    ), f"Expected 'a few seconds ago', got {relative_time(seconds_ago_40)}"
    assert (
        relative_time(minutes_ago_40) == "40 minutes ago"
    ), f"Expected '40 minutes ago', got {relative_time(minutes_ago_40)}"
    assert (
        relative_time(hours_ago_7) == "7 hours ago"
    ), f"Expected '7 hours ago', got {relative_time(hours_ago_7)}"
    assert (
        relative_time(days_ago_3) == "3 days ago"
    ), f"Expected '3 days ago', got {relative_time(days_ago_3)}"
    assert (
        relative_time(weeks_ago_3) == "3 weeks ago"
    ), f"Expected '3 weeks ago', got {relative_time(weeks_ago_3)}"
    assert (
        relative_time(months_ago_3) == "3 months ago"
    ), f"Expected '3 months ago', got {relative_time(months_ago_3)}"
    assert (
        relative_time(years_ago_3) == "3 years ago"
    ), f"Expected '3 years ago', got {relative_time(years_ago_3)}"


if __name__ == "__main__":
    test_relative_time()
