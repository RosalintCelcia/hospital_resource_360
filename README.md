# 🏥 Hospital Resource 360: Intelligent Optimization Dashboard

### 🚀 A Full-Stack Analytics Solution for Healthcare Operations
**Participant:** HCL Guvi Career Carnival Hackathon 2026

![Status](https://img.shields.io/badge/Status-Completed-success)
![Tech](https://img.shields.io/badge/Stack-Python%20|%20MySQL%20|%20PowerBI-blue)

## 📖 Project Overview
Hospital Resource 360 is a data-driven analytics platform designed to solve operational bottlenecks in multi-specialty hospitals. By integrating a **Python/MySQL backend** with a **Power BI frontend**, this tool provides real-time visibility into patient flow, doctor utilization, and revenue streams.

It features **AI-driven forecasting** to predict patient admission trends for the next 14 days, allowing administrators to move from reactive to proactive staffing.

## 📸 Dashboard Screenshots
*<img width="1333" height="778" alt="Image" src="https://github.com/user-attachments/assets/d61e0d70-4c69-4ff9-8e8e-5cd85e195d70" />*

## ✨ Key Features
* **🤖 AI Predictive Analytics:** Forecasts future patient volume using time-series modeling to prevent overcrowding.
* **🚨 Bottleneck Detection:** Automatically highlights departments with high Average Length of Stay (ALOS) and readmission rates.
* **💰 Revenue Intelligence:**Breakdown of revenue streams by insurance type (Govt Scheme, Private, Self-Pay).
* **👨‍⚕️ Doctor Utilization:** Leaderboards tracking specialist workload and patient outcomes.
* **⚡ Interactive Slicing:** Dynamic filtering by Department and Admission Status.

## 🛠️ Tech Stack
* **Backend:** Python (FastAPI) & SQLAlchemy
* **Data Processing:** Pandas (ETL Pipeline) & Faker (Synthetic Data Generation)
* **Database:** MySQL 8.0 (Relational Schema)
* **Visualization:** Microsoft Power BI (DAX Measures & Forecasting)

## ⚙️ How to Run Locally

### Prerequisites
* Python 3.10+
* MySQL Server
* Power BI Desktop

### Step 1: Clone the Repo
```bash
git clone [https://github.com/YOUR_USERNAME/hospital-resource-360.git](https://github.com/YOUR_USERNAME/hospital-resource-360.git)
cd hospital-resource-360
```

### Step 2: Install Dependencies
```bash
pip install fastapi uvicorn pandas faker sqlalchemy pymysql
```

### Step 3: Setup Database & Run Backend
Open main.py and update the DATABASE_URL with your MySQL credentials. Then run:

```bash
python main.py
```

This will automatically generate 1,000 synthetic patient records and populate your local MySQL database.

### Step 4: View Analytics
1.Open Hospital_Dashboard.pbix in Power BI.

2.Click Refresh to load the data from your local database.

3.Interact with the dashboard!

### 📊 Business Impact
- Reduces Wait Times: By identifying peak traffic days.
- Optimizes Staffing: Matches doctor schedules to predicted patient inflow.
- Increases Revenue: Identifies high-value insurance segments.
