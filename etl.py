import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Loop on create table queries from `copy_table_queries` variable defined in `sql_queries.py` and Execute them
    :param cur: cursor to DB
    :param conn: connection to DB
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Loop on create table queries from `insert_table_queries` variable defined in `sql_queries.py` and Execute them
    :param cur: cursor to DB
    :param conn: connection to DB
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Driver Function
    Read `dwh.cfg` file to fetch DB conn info
    Create connection to DB and get cur, conn
    Load Data into staging table, Populate data from staging to final tables
    Close Connection
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
