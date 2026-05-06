# Personal BI & Data Engineering Lab

A modern end-to-end Data Engineering and Business Intelligence ecosystem built on a local environment. This project demonstrates a production-grade data stack for personal finance and lifestyle analytics.

## 🚀 Project Overview
This project simulates a professional data lifecycle: from synthetic data generation and orchestration to containerized storage and interactive visualization. It serves as a digital twin for personal expense monitoring.

### Core Capabilities
- **Automated Orchestration**: Managed by **Dagster**, using Software-Defined Assets (SDA) to handle data dependencies.
- **Realistic Data Simulation**: Utilizes the **Faker** library to generate complex, real-world financial transaction patterns.
- **Containerized Database**: A **PostgreSQL** 15 instance running on **Docker**, serving as the central data warehouse.
- **Interactive BI**: Connected to **Tableau Public** for advanced visual analytics and lifestyle clustering.

## 🏗️ Technical Architecture
The pipeline is structured as a Directed Acyclic Graph (DAG):
1. **Source (Python/Faker)**: Generates synthetic transactions and payroll data.
2. **Orchestration (Dagster)**: Coordinates the flow from Python scripts to the database.
3. **Storage (PostgreSQL)**: Stores raw data in a relational format.
4. **Presentation (Tableau)**: Visualizes cash flow, spending categories, and lifestyle habits.

## 🛠️ Tech Stack
- **Languages**: Python 3.13
- **Orchestration**: Dagster
- **Database**: PostgreSQL (Docker)
- **Data Manipulation**: Pandas, SQLAlchemy
- **Visualization**: Tableau Public

## 🏁 Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/)
- Python 3.10+ (venv recommended)

### Setup & Run
1. **Start the database**:
   ```bash
   docker compose up -d