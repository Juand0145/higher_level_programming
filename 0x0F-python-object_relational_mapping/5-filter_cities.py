#!/usr/bin/python3
"""Is a a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""

from MySQLdb import DATE

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states \
        ON states.id = cities.state_id WHERE states.name = '{}' \
            ORDER BY cities.id ASC".format(argv[4]))
    rows = cur.fetchall()

    print(", ".join(row[0] for row in rows))

    db.close()
