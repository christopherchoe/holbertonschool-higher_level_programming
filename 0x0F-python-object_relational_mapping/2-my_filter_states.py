#!/usr/bin/python3
"""
script to list all states from hbtn_0e_0_usa matching argument
"""


if __name__ == "__main__":
    import MySQLdb
    import sqlalchemy
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE BINARY states.name = '{}' ORDER BY \
        states.id".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
