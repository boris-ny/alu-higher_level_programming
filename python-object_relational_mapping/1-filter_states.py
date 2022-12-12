#!/usr/bin/python3
""" A script that lists all states with a name starting with N (upper N)"""

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
    ora.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for row in ora.fetchall():
        if row[1][0] == 'N':
            print(row)
    ora.close()
    db_get.close()
