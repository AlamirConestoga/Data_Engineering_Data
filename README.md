What This Project Does
Database Setup: Sets up an employees table on a free Neon PostgreSQL database.

Data Generation: Uses Python and Faker to generate 100 fake employee records with realistic salaries and start dates.

Data Analysis: Generates charts using Seaborn and Plotly to analyze salary and tenure trends across departments.

Database Table Structure
SQL
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    start_date DATE CHECK (start_date >= '2015-01-01' AND start_date <= '2024-12-31'),
    salary INT CHECK (salary >= 60000 AND salary <= 200000)
);


Quick Start
1. Install Dependencies
Bash
pip install -r requirements.txt
2. Add Database Link
Open data_generation.py and replace DATABASE_URL with your Neon connection string:

Python
DATABASE_URL = "postgresql://user:password@ep-sample.aws.neon.tech/neondb?sslmode=require"
3. Run Data Generation
Bash
python data_generation.py
Main Insights
Tenure vs. Pay: Average years of service do not strongly affect average salary levels across departments.

Top Earners: Marketing and Administration recorded the highest peak salaries in specific hire years.

Tenure Trend: Tenure declines steadily from earlier hires (2019) down to recent hires (2024).