# Automated Data Ingestion & Reporting Pipeline

## 📌 Project Overview

This project demonstrates a **fully automated data pipeline** built with Python. The pipeline ingests raw CSV files, cleans and standardizes the data, and produces processed datasets and summary reports — all executed with a single command.

The focus of this project is **automation, reproducibility, and clean data workflows**, rather than dashboards or manual analysis.

---

## 🎯 Objectives

* Automate ingestion of multiple raw CSV files
* Apply consistent data cleaning and validation rules
* Generate processed datasets ready for analysis
* Automatically produce summary reports
* Demonstrate end-to-end pipeline structure (Extract → Transform → Load)

---

## 🧱 Project Structure

```
project-2-automation-pipeline/
│
├── data/
│   ├── raw/           # Input CSV files
│   └── processed/     # Cleaned output data
│
├── reports/            # Automatically generated reports
│
├── src/
│   ├── __init__.py
│   ├── extract.py     # Data ingestion logic
│   ├── transform.py   # Cleaning & validation logic
│   ├── load.py        # Output & reporting logic
│   └── main.py        # Pipeline orchestrator
│
├── requirements.txt
└── README.md
```

---

## 🔄 Pipeline Steps

### 1️⃣ Extract

* Automatically reads **all CSV files** from `data/raw/`
* Combines them into a single dataset
* Tracks source file names for traceability

### 2️⃣ Transform

* Standardizes column names
* Removes duplicate records
* Handles missing values
* Ensures consistent schema

### 3️⃣ Load

* Saves cleaned data to `data/processed/cleaned_data.csv`
* Generates a statistical summary report in `reports/summary_report.csv`

---

## ▶️ How to Run

### 1. Create virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add raw data

Place one or more CSV files into:

```
data/raw/
```

### 4. Run the pipeline

From the **project root**:

```bash
python -m src.main
```

---

## Outputs

After execution, the pipeline generates:

* `data/processed/cleaned_data.csv`
* `reports/summary_report.csv`

All outputs are created automatically.

---

##  Key Skills Demonstrated

* Python automation
* Modular ETL pipeline design
* Data cleaning & validation
* File system orchestration
* Reproducible workflows

---

##  Next Improvements (Planned)

* API-based ingestion
* Database loading (SQLite / PostgreSQL)
* Logging & error handling
* Scheduling (cron / Task Scheduler)

---


