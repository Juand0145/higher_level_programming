#!/usr/bin/python3

"""Is a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM\
         cities LEFT JOIN states ON states.id = cities.state_id\
         ORDER BY cities.id ASC;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    db.close()
