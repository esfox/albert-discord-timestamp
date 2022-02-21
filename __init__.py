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
        {
            "modifier": "f",
            "text": time.strftime("%-d %B %Y %I:%M", date_to_convert.timetuple()),
            "subtext": "Short Date/Time",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:f>",
        },
        {
            "modifier": "F",
            "text": time.strftime("%A, %-d %B %Y %I:%M", date_to_convert.timetuple()),
            "subtext": "Long Date/Time",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:F>",
        },
        {
            "modifier": "t",
            "text": time.strftime("%I:%M", date_to_convert.timetuple()),
            "subtext": "Short Time",
            "icon": TIME_ICON,
            "clipboardText": f"<t:{unix_timestamp}:t>",
        },
        {
            "modifier": "T",
            "text": time.strftime("%I:%M:%S", date_to_convert.timetuple()),
            "subtext": "Long Time",
            "icon": TIME_ICON,
            "clipboardText": f"<t:{unix_timestamp}:T>",
        },
        {
            "modifier": "d",
            "text": time.strftime("%m/%d/%Y", date_to_convert.timetuple()),
            "subtext": "Short Date",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:d>",
        },
        {
            "modifier": "D",
            "text": time.strftime("%-d %B %Y", date_to_convert.timetuple()),
            "subtext": "Long Date",
            "icon": DATE_ICON,
            "clipboardText": f"<t:{unix_timestamp}:D>",
        },
        {
            "modifier": "R",
            "text": time.strftime("%I:%M", date_to_convert.timetuple()),
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
