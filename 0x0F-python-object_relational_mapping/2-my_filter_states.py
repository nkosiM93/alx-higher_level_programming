#!/usr/bin/python3
""" Module uses MySQLdb to connect to a database and retrieve info """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute(f"USE {sys.argv[3]}")
    cur.execute(f"SELECT * FROM states WHERE BINARY name = {sys.argv[4]} "
                "ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(f"{row}")
