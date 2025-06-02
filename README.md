# 🚀 ETL Data Pipeline with Apache Airflow & Docker

This project demonstrates a containerized **ETL (Extract, Transform, Load)** pipeline using **Apache Airflow**, orchestrated via **Docker**.

---

## 📌 Features

- ⛏️ **Extract**: Reads `input.csv` with transaction data.
- 🔄 **Transform**: Filters rows with `amount > 100`.
- 📤 **Load**: Saves the filtered data to `output/output.csv`.
- 📧 **Email Notification**: Sends an email with the result file attached after the DAG completes.
- 🔁 **Scheduled** to run daily via Airflow's scheduler.
- 🐳 **Dockerized** for portable, reproducible setup.

---

## 🛠️ Tech Stack

- **Python**
- **Apache Airflow**
- **Docker / Docker Compose**
- **Pandas** for data manipulation

---

## 📂 Project Structure

```bash
.
├── dags/
│   └── etl_data_pipeline.py        # Airflow DAG definition
├── input/
│   └── input.csv                   # Sample input data
├── output/
│   └── output.csv                  # Output after ETL
├── docker-compose.yml             # Airflow + Docker config
└── README.md                       # You're here
