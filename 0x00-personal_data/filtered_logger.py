#!/usr/bin/env python3
"""filter data"""
import re
import logging
from typing import List
import mysql.connector
import os


patterns = {
    'extract': lambda x, y: r"(?P<field>{})=[^{}]*".format("|".join(x), y),
    'replace': lambda x: r"\g<field>={}".format(x),
}
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Function to create a connector to mysql db"""
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_psswd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    connnection = mysql.connector.connect(
        host=db_host,
        port=3306,
        user=db_user,
        password=db_psswd,
        database=db_name,
    )
    return connnection


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Function to filter data using Regex"""
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)


def get_logger() -> logging.Logger:
    """Function to create a logger"""
    logger = logging.getLogger("user_data")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(stream_handler)
    return logger


def main():
    """main function"""
    fields = "name,email,phone,ssn,password,ip,last_login,user_agent"
    col = fields.split(',')
    query = "SELECT {} FROM users".format(fields)
    log = get_logger()
    connection = get_db()
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            record = map(
                lambda x: "{}={}".format(x[0], x[1]),
                zip(col, row)
            )
            msg = "{};".format("; ".join(list(record)))
            args = ("user_data", logging.INFO, None, None, msg, None, None)
            log_record = logging.LogRecord(*args)
            log.handle(log_record)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ("name", "levelname", "asctime", "message")
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Function to format login info"""
        msg = super(RedactingFormatter, self).format(record)
        txt = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        return txt


if __name__ == "__main__":
    main()
