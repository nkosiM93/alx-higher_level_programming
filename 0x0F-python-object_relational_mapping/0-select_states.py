#!/usr/bin/python3
""" Module uses MySQLdb to connect to a database and retrieve info """
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="hbtn_0e_0_usa")
    cur = db.cursor()

    cur.execute("USE hbtn_0e_0_usa")
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(f"{row}")
