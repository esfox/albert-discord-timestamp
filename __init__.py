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
        # Short Date/Time (e.g. "August 28, 2021 4:08 AM")
        {
            "modifier": "f",
            "text": date_to_convert.strftime('%B %-d, %Y %-I:%M %p'),
            "subtext": "Short Date/Time",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:f>",
        },
        # Long Date/Time (e.g. "Saturday, August 28, 2021 4:08 AM")
        {
            "modifier": "F",
            "text": date_to_convert.strftime('%A, %B %-d, %Y %-I:%M %p'),
            "subtext": "Long Date/Time",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:F>",
        },
        # Short Time (e.g. "4:08 AM")
        {
            "modifier": "t",
            "text": date_to_convert.strftime('%-I:%M %p'),
            "subtext": "Short Time",
            "icon": TIME_ICON,
            "clipboardText": f"<t:{unix_timestamp}:t>",
        },
        # Long Time (e.g. "4:08:48 AM")
        {
            "modifier": "T",
            "text": date_to_convert.strftime('%-I:%M:%S %p'),
            "subtext": "Long Time",
            "icon": TIME_ICON,
            "clipboardText": f"<t:{unix_timestamp}:T>",
        },
        # Short Date (e.g. "08/28/2021")
        {
            "modifier": "d",
            "text": date_to_convert.strftime('%m/%d/%Y'),
            "subtext": "Short Date",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:d>",
        },
        # Long Date (e.g. "August 28, 2021")
        {
            "modifier": "D",
            "text": date_to_convert.strftime('%B %-d, %Y'),
            "subtext": "Long Date",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:D>",
        },
        # Relative Time (e.g. "in 2 hours")
        {
            "modifier": "R",
            "text": date_to_convert.strftime('%-I:%M %p'),
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
