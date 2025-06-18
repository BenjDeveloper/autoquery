#!/usr/bin/env python3
import os
import sys
import pymysql
import pandas as pd
import re


def read_query(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.search(r'```sql\s*(.*?)\s*```', content, re.DOTALL | re.IGNORECASE)
        if match:
            query = match.group(1).strip()
        else:
            query = content.strip()
        return query
    except Exception as e:
        print(f"[ERROR] Could not read file {file_path}: {e}")
        sys.exit(1)


def execute_query(query):
    conn_params = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "",
        "database": "dbtest"
    }
    try:
        conn = pymysql.connect(**conn_params)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall() if cur.description else []
        colnames = [desc[0] for desc in cur.description] if cur.description else []
        conn.commit()
        cur.close()
        conn.close()
        return rows, colnames
    except Exception as e:
        print(f"[ERROR] Query execution failed: {e}")
        return None, None


def main():
    query_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "respuesta.txt")
    query = read_query(query_file)
    print("[DEBUG] Running query:\n", query)

    rows, colnames = execute_query(query)
    if rows is None:
        print("[INFO] Query failed. A new query is required.")
        sys.exit(1)
    else:
        print("[DEBUG] Query executed successfully.")
        success_query_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "respuesta_existosa.txt")
        with open(success_query_file, "w", encoding="utf-8") as f:
            f.write(query)
        print(f"[DEBUG] Successful query saved at: {success_query_file}")

        df = pd.DataFrame(rows, columns=colnames)
        csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.csv")
        df.to_csv(csv_file, index=False)
        print(f"[DEBUG] Data saved to: {csv_file}")


if __name__ == "__main__":
    main()
