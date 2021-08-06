#!/usr/bin/python3

"""Is a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute(
        f"SELECT * FROM states WHERE name LIKE {argv[4]} ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    db.close()
