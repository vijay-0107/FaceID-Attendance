import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn , table):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + str(table[0]))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def show_all_tables(conn):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    return rows


def main():
    database = "./db.sqlite3"

    # create a database connection
    conn = create_connection(database)
    with conn:

        # print("2. Query all tasks")
        # select_all_tasks(conn)

        tables = show_all_tables(conn)
        for table in tables : 
            select_all_tasks(conn , table)
            print(100*'*')


if __name__ == '__main__':
    main()