import os
import psycopg2
from pathlib import Path

PARAMS = {
    "dbname": os.environ["DB"],
    "user": os.environ["PG_USER"],
    "password": os.environ["PG_PASSWORD"],
    "host": "localhost",
    "port": "5432",
}
CREATE_TABLE_FILE = "create_table.sql"
INSERT_TABLE_QUERY = "INSERT INTO oac_tw_table ({}) VALUES ({})"


def get_db_connection():
    conn = psycopg2.connect(**PARAMS)
    return conn


def create_table(conn):
    with conn.cursor() as cursor:
        create_table_path = Path(Path(__file__).parent, CREATE_TABLE_FILE)

        with open(create_table_path) as f:
            query = f.read()
        cursor.execute(query)
    conn.commit()


def insert_into_table(conn, df):
    with conn.cursor() as cursor:
        columns = ", ".join(df.columns)
        placeholders = ", ".join(["%s"] * len(df.columns))
        query = INSERT_TABLE_QUERY.format(columns, placeholders)
        rows = [tuple(row) for row in df.values]
        cursor.executemany(query, rows)
        return len(rows)
    conn.commit()
