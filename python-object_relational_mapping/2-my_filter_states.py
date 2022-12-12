#!/usr/bin/python3
""" A script that takes in an argument and displays all values in the states table."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_get = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3])

    ora = db_get.cursor()
    ora.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4],))

    for row in ora.fetchall():
        if row[1] == argv[4]:
            print(row)
    ora.close()
    db_get.close()
