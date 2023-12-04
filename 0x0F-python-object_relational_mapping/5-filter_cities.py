#!/usr/bin/python3
"""Script contains code that filters cities from a specific state entered"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cities = cur.execute("SELECT cities.name FROM cities JOIN states "
                         "ON cities.state_id = states.id "
                         f"WHERE states.name = '{sys.argv[4]}'")
    cities = cur.fetchall()

    for j in range(len(cities)):
        for i in range(len(cities[j])):
            print(f"{cities[j][i]}", end="")
            if j != len(cities) - 1:
                print(", ", end="")
            else:
                print()
