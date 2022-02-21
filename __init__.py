# -*- coding: utf-8 -*-

"""
Discord Timestamp Generator
"""

from albert import *
import os
import time

__title__ = "Discord Timestamp Generator"
__version__ = "0.0.1"
__triggers__ = ["dt"]
__authors__ = "esfox"

currentPath = os.path.dirname(__file__)
timeIcon = f"{currentPath}/time.svg"
dateIcon = f"{currentPath}/date.svg"
relativeTimeIcon = f"{currentPath}/relative-time.svg"

def handleQuery(query):

    if not query.isTriggered:
        return

    currentTimeSeconds = round(time.time())
    formats = [
        {
            "modifier": "f",
            "text": time.strftime('%-d %B %Y %I:%M'),
            "subtext": "Short Date/Time",
            "icon": dateIcon,
            "clipboardText": f"<t:{currentTimeSeconds}:f>",
        },
        {
            "modifier": "F",
            "text": time.strftime('%A, %-d %B %Y %I:%M'),
            "subtext": "Long Date/Time",
            "icon": dateIcon,
            "clipboardText": f"<t:{currentTimeSeconds}:F>",
        },
        {
            "modifier": "t",
            "text": time.strftime('%I:%M'),
            "subtext": "Short Time",
            "icon": timeIcon,
            "clipboardText": f"<t:{currentTimeSeconds}:t>",
        },
        {
            "modifier": "T",
            "text": time.strftime('%I:%M:%S'),
            "subtext": "Long Time",
            "icon": timeIcon,
            "clipboardText": f"<t:{currentTimeSeconds}:T>",
        },
        {
            "modifier": "d",
            "text": time.strftime('%m/%d/%Y'),
            "subtext": "Short Date",
            "icon": dateIcon,
            "clipboardText": f"<t:{currentTimeSeconds}:d>",
        },
        {
            "modifier": "D",
            "text": time.strftime('%-d %B %Y'),
            "subtext": "Long Date",
            "icon": dateIcon,
            "clipboardText": f"<t:{currentTimeSeconds}:D>",
        },
        {
            "modifier": "R",
            "text": time.strftime('%I:%M'),
            "subtext": "Relative Time",
            "icon": relativeTimeIcon,
            "clipboardText": f"<t:{currentTimeSeconds}:R>",
        },
    ]

    items = []
    for i, format in enumerate(formats):
        items.append(Item(
            id=str(i),
            text=format["text"],
            subtext=format["subtext"],
            icon=format["icon"],
            actions=[
                ClipAction(
                    text=format["subtext"],
                    clipboardText=format["clipboardText"]
                )
            ],
        ))

    return items
