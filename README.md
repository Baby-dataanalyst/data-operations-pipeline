# Data Operations Pipeline Validator

Small Python scripts to generate sample pipeline output data and validate daily load quality checks.

## Files

- `csv_data.py`: Creates a sample `pipeline_output.csv` file for testing.
- `pipeline_validator.py`: Validates today's records for duplicates, nulls, and status counts, then writes a report.

## Requirements

- Python 3.8+
- `pandas`

Install dependency:

```bash
pip install pandas
```

## Usage

1. Generate sample CSV:

```bash
python csv_data.py
```

2. Run validator:

```bash
python pipeline_validator.py
```

3. Check generated report file:

- `pipeline_report_<YYYY-MM-DD>.txt`

## What the validator checks

- Records loaded for today
- Duplicate `customer_id` values
- Null values per column
- Status distribution (for example: `SUCCESS`, `FAILED`)

## Background

Built based on real production operations experience supporting AWS and GCP 
data pipelines at Accenture for global enterprise clients. The validation 
logic mirrors day-to-day data quality checks performed during live pipeline 
monitoring for Ingredion (GCP/Airflow) and Essilor (AWS batch pipeline).
