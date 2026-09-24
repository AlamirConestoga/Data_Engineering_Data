import pandas as pd
import psycopg2

from data.cloud_data_collection import DATABASE_URL, insert_employee_records


def main():
    insert_employee_records()

   
    with psycopg2.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]

    df = pd.DataFrame(rows, columns=columns)

    print(df.head())


main()


