import sqlite3
import pandas as pd


def execute_query(table_name, data, sql_query):

    conn = sqlite3.connect(":memory:")

    df = pd.DataFrame(data)

    df.to_sql(
        table_name,
        conn,
        index=False,
        if_exists="replace"
    )

    result_df = pd.read_sql_query(
        sql_query,
        conn
    )

    conn.close()

    return result_df.to_dict(orient="records")