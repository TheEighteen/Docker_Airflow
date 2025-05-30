from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta
import pandas as pd
import os

# DAG configuration
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
}

# File paths that match your Docker volume mappings
INPUT_DIR = '/usr/local/airflow/input'
OUTPUT_DIR = '/usr/local/airflow/output'
INPUT_FILE = os.path.join(INPUT_DIR, 'input.csv')
EXTRACTED_FILE = os.path.join(INPUT_DIR, 'extracted.csv')
TRANSFORMED_FILE = os.path.join(INPUT_DIR, 'transformed.csv')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'output.csv')

# Task 1: Extract
def extract():
    df = pd.read_csv(INPUT_FILE)
    df.to_csv(EXTRACTED_FILE, index=False)
    print("Extracted data:")
    print(df)

# Task 2: Transform
def transform():
    df = pd.read_csv(EXTRACTED_FILE)
    df_filtered = df[df['amount'] > 100]  # Only rows with amount > 100
    df_filtered.to_csv(TRANSFORMED_FILE, index=False)
    print("Transformed data (amount > 100):")
    print(df_filtered)

# Task 3: Load
def load():
    df = pd.read_csv(TRANSFORMED_FILE)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Loaded data saved to {OUTPUT_FILE}")

# Define the DAG
with DAG(
    dag_id='etl_data_pipeline',
    default_args=default_args,
    description='ETL pipeline for input.csv',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 5, 30),
    catchup=False,
    tags=['etl', 'csv'],
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load,
    )

    email_task = EmailOperator(
        task_id='send_email',
        to='ursvinayk18@gmail.com',  # <-- Replace with your actual email
        subject='ETL Job Finished - Output CSV',
        html_content='<p>The ETL job has completed. Find the output attached.</p>',
        files=[OUTPUT_FILE],
    )

    # Define task order
    extract_task >> transform_task >> load_task >> email_task
