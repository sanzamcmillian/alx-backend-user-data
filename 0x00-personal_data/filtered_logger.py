#!/usr/bin/env python3
""""""
import re
from typing import List


patterns = {
    'extract': lambda x, y: r"(?P<field>{})=[^{}]*".format("|".join(x), y),
    'replace': lambda x: r"\g<field>={}".format(x),
}


def filter_datum(fields, redaction, message, separator):
    """Function to filter data using Regex"""
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
