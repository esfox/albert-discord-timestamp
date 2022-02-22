# -*- coding: utf-8 -*-

"""
Discord Timestamp Generator
"""

from datetime import datetime
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
            # TODO: make this show the relative time
            "text": date_to_convert.strftime(LOCALE_FORMATS[LOCALE]["t"]),
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
