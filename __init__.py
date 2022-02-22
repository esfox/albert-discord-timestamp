# -*- coding: utf-8 -*-

"""
Discord Timestamp Generator
"""

from datetime import datetime, timedelta
import os
import time
from typing import List, Optional

import albert
import dateparser

__title__ = "Discord Timestamp Generator"
__version__ = "0.1.0"
__triggers__ = ["dt"]
__authors__ = "esfox"
__py_deps__ = ["dateparser"]

LOCALE = "en-GB"  # this can be configured to any of the formats appearing below

LOCALE_FORMATS = {
    "en-GB": {
        "t": "%H:%S",  # 04:08
        "T": "%H:%S:%S",  # 04:08:48
        "d": "%d/%m/%Y",  # 28/08/2021
        "D": "%-d %B %Y",  # 28 August 2021
        "f": "%-d %B %Y %H:%S",  # 28 August 2021 04:08
        "F": "%A, %-d %B %Y %H:%S",  # Saturday, 28 August 2021 04:08
    },
    "en-US": {
        "t": "%-I:%M %p",  # 4:08 AM
        "T": "%-I:%M:%S %p",  # 4:08:48 AM
        "d": "%m/%d/%Y",  # 08/28/2021
        "D": "%B %-d, %Y",  # August 28, 2021
        "f": "%B %-d, %Y %-I:%M %p",  # August 28, 2021 4:08 AM
        "F": "%A, %B %-d, %Y %-I:%M %p",  # Saturday, August 28, 2021 4:08 AM
    },
}

PATH = os.path.dirname(__file__)
TIME_ICON = f"{PATH}/time.svg"
DATE_ICON = f"{PATH}/date.svg"
RELATIVE_TIME_ICON = f"{PATH}/relative-time.svg"


def relative_time(date: datetime) -> str:
    """
    Returns a humanized string representing time difference
    between now() and the input datetime object

    eg. "2 minutes ago", "in 11 months", "a day ago", etc.
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


def handleQuery(query: albert.Query) -> Optional[List[albert.Item]]:

    if not query.isTriggered:
        return

    date_to_convert = datetime.now()

    if query_string := query.string.strip():
        albert.info(f"Parsing query string: {query_string} as date")
        date_to_convert = dateparser.parse(query_string)
        albert.info(f"Date was parsed as {date_to_convert}")

    if date_to_convert is None:
        return [
            albert.Item(
                text=f"Couldn't parse date: {query_string}",
                subtext="Please try again",
                icon=TIME_ICON,
            )
        ]

    unix_timestamp = int(time.mktime(date_to_convert.timetuple()))
    albert.info(f"Showing results for the timestamp: {unix_timestamp}")

    formats = [
        {
            "modifier": "f",
            "text": date_to_convert.strftime(LOCALE_FORMATS[LOCALE]["f"]),
            "subtext": "Short Date/Time",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:f>",
        },
        {
            "modifier": "F",
            "text": date_to_convert.strftime(LOCALE_FORMATS[LOCALE]["F"]),
            "subtext": "Long Date/Time",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:F>",
        },
        {
            "modifier": "t",
            "text": date_to_convert.strftime(LOCALE_FORMATS[LOCALE]["t"]),
            "subtext": "Short Time",
            "icon": TIME_ICON,
            "clipboardText": f"<t:{unix_timestamp}:t>",
        },
        {
            "modifier": "T",
            "text": date_to_convert.strftime(LOCALE_FORMATS[LOCALE]["T"]),
            "subtext": "Long Time",
            "icon": TIME_ICON,
            "clipboardText": f"<t:{unix_timestamp}:T>",
        },
        {
            "modifier": "d",
            "text": date_to_convert.strftime(LOCALE_FORMATS[LOCALE]["d"]),
            "subtext": "Short Date",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:d>",
        },
        {
            "modifier": "D",
            "text": date_to_convert.strftime(LOCALE_FORMATS[LOCALE]["D"]),
            "subtext": "Long Date",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:D>",
        },
        {
            "modifier": "R",
            "text": relative_time(date_to_convert),
            "subtext": "Relative Time",
            "icon": RELATIVE_TIME_ICON,
            "clipboardText": f"<t:{unix_timestamp}:R>",
        },
    ]

    items = []
    for i, format in enumerate(formats):
        items.append(
            albert.Item(
                id=str(i),
                text=format["text"],
                subtext=format["subtext"],
                icon=format["icon"],
                actions=[
                    albert.ClipAction(
                        text=format["subtext"], clipboardText=format["clipboardText"]
                    )
                ],
            )
        )

    return items
