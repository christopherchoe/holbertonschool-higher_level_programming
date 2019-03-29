#!/usr/bin/python3
"""
script to list all states from hbtn_0e_0_usa that start with N
"""


if __name__ == "__main__":
    import MySQLdb
    import sqlalchemy
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE BINARY states.name LIKE 'N%' ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
