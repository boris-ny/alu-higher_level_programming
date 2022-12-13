#!/usr/bin/python3
"""A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_get = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    ora = db_get.cursor()
    ora.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))

    cites = []
    for row in ora.fetchall():
        cites.append(row[0])

    print(", ".join(cites))
    ora.close()
    db_get.close()
