import os
import random
from datetime import date
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from faker import Faker
from streamlit import connection

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

fake_data = Faker()

POSITIONS = [
    "Accountant",
    "HR Specialist",
    "Marketing Manager",
    "Sales Representative",
    "Financial Analyst",
    "Operations Manager",
    "Graphic Designer",
    "Customer Support Representative",
    "Logistics Coordinator",
    "Executive Assistant",
]


def generate_employee_records(count: int = 100):
    for emp_id in range(1, count + 1):
        yield (
            emp_id,
            fake_data.name(),
            random.choice(POSITIONS),
            fake_data.date_between(start_date=date(2015, 1, 1), end_date=date(2024, 12, 31)),
            random.randint(60000, 200000),
        )


def insert_employee_records(count: int = 100):
    with psycopg2.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            for employee in generate_employee_records(count):
                cursor.execute(
                    """
                    INSERT INTO employees (employee_id, name, position, start_date, salary)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (employee_id) DO NOTHING
                    """,
                    employee,
                )

    print(f"{count} synthetic employee records inserted into the cloud database successfully.")

    

