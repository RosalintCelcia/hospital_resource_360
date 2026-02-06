Project: Hospital 360 - Resource Optimization Dashboard
Team Member: Rosalint Celcia J

FILES INCLUDED:
1. main.py (Backend Data Generator & API)
2. Hospital_Dashboard.pbix (Interactive Analytics)
3. Hospital_Monthly_Report.pdf (Automated Reporting Output)

HOW TO RUN:
1. Install requirements: pip install fastapi uvicorn pandas faker sqlalchemy pymysql
2. Run the backend: python main.py
   (This will automatically populate the MySQL database with fresh data)
3. Open 'Hospital_Dashboard.pbix' in Power BI.
4. Click 'Refresh' to see the new data.

KEY FEATURES:
- AI Forecasting for patient admissions (Line Chart).
- Real-time Bottleneck Detection (Bar Chart).
- Interactive Slicing by Department & Insurance.