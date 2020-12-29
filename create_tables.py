import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Loop on create table queries from `drop_table_queries` variable defined in `sql_queries.py` and Execute them
    :param cur: cursor to DB
    :param conn: connection to DB
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Loop on create table queries from `create_table_queries` variable defined in `sql_queries.py` and Execute them
    :param cur: cursor to DB
    :param conn: connection to DB
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Driver function:
    Read `dwh.cfg` file to fetch DB conn info
    Create connection to DB and get cur, conn
    Drop Tables, Create Tables
    Close Connection
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
