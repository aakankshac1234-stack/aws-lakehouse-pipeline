# AWS Lakehouse Pipeline

## Overview

End-to-end cloud-native data engineering pipeline built on AWS using a Lakehouse architecture.

## Technologies

* Python
* PySpark
* AWS S3
* AWS Glue
* Amazon Redshift
* Apache Airflow
* dbt
* Terraform

## Features

* Ingests large-scale datasets into Amazon S3
* Processes Bronze, Silver, and Gold layers using PySpark
* Implements data quality checks and validation
* Builds dimensional models in Redshift using dbt
* Automated orchestration with Apache Airflow
* Infrastructure managed with Terraform

## Architecture

Source Data → S3 → AWS Glue/PySpark → Redshift → BI Dashboard

## Outcomes

* Scalable analytics platform
* Automated ETL workflows
* Data quality monitoring
* Cost-efficient cloud architecture
