# ETL Data Pipeline with Airflow & Docker

This project demonstrates an end-to-end ETL pipeline using Apache Airflow inside Docker.

## Features
- Extracts data from `input.csv`
- Transforms rows where amount > 100
- Loads result to `output/output.csv`
- Sends email alert on completion

## Tech Stack
- Python
- Apache Airflow
- Docker
