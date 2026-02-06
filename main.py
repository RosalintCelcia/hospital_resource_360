import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
from fastapi import FastAPI
import uvicorn
from sqlalchemy import create_engine, text

app = FastAPI()
fake = Faker('en_IN')

# --- CONFIGURATION ---
# UPDATE THIS LINE: mysql+pymysql://username:password@host:port/database_name
# If your password is 'root' or '1234', put it after 'root:'
DATABASE_URL = "mysql+pymysql://root:rose@localhost:3306/hospital_db"

engine = create_engine(DATABASE_URL)

NUM_PATIENTS = 500
NUM_ADMISSIONS = 1000
DEPARTMENTS = [
    ('Cardiology', 20), ('Oncology', 15), ('Orthopedics', 25),
    ('Pediatrics', 15), ('Emergency', 10), ('General Medicine', 30)
]
INSURANCE = ['Star Health', 'LIC', 'Govt Scheme', 'Self Pay']
OUTCOMES = ['Recovered', 'Improved', 'Transferred', 'Deceased']

# --- DATA GENERATION ---
def generate_and_upload():
    print("Generating data...")
    
    # 1. Departments
    depts = [{'name': d[0], 'total_beds': d[1]} for d in DEPARTMENTS]
    df_dept = pd.DataFrame(depts)
    df_dept.to_sql('departments', engine, if_exists='append', index=False)
    print(" - Departments uploaded")

    # Fetch IDs to ensure relationships work
    with engine.connect() as conn:
        dept_ids = [row[0] for row in conn.execute(text("SELECT dept_id FROM departments")).fetchall()]

    # 2. Doctors
    doctors = []
    for _ in range(30):
        doctors.append({
            'name': fake.name(),
            'dept_id': random.choice(dept_ids),
            'specialization': 'Specialist'
        })
    df_docs = pd.DataFrame(doctors)
    df_docs.to_sql('doctors', engine, if_exists='append', index=False)
    print(" - Doctors uploaded")

    with engine.connect() as conn:
        doc_ids = [row[0] for row in conn.execute(text("SELECT doc_id FROM doctors")).fetchall()]

    # 3. Patients
    patients = []
    for _ in range(NUM_PATIENTS):
        patients.append({
            'age': random.randint(1, 90),
            'gender': random.choice(['Male', 'Female']),
            'insurance_type': random.choice(INSURANCE),
            'city': fake.city()
        })
    df_patients = pd.DataFrame(patients)
    df_patients.to_sql('patients', engine, if_exists='append', index=False)
    print(" - Patients uploaded")

    with engine.connect() as conn:
        pat_ids = [row[0] for row in conn.execute(text("SELECT patient_id FROM patients")).fetchall()]

    # 4. Admissions
    admissions = []
    start_date = datetime(2025, 1, 1) # Updated for current year context
    for _ in range(NUM_ADMISSIONS):
        adm_date = start_date + timedelta(days=random.randint(0, 365))
        los = random.randint(1, 15)
        dis_date = adm_date + timedelta(days=los)
        
        admissions.append({
            'patient_id': random.choice(pat_ids),
            'doc_id': random.choice(doc_ids),
            'dept_id': random.choice(dept_ids),
            'admission_date': adm_date,
            'discharge_date': dis_date,
            'admission_type': random.choice(['Emergency', 'Elective']),
            'status': 'Discharged',
            'outcome': random.choice(OUTCOMES),
            'billing_amount': random.randint(5000, 200000)
        })
    df_admissions = pd.DataFrame(admissions)
    df_admissions.to_sql('admissions', engine, if_exists='append', index=False)
    print(" - Admissions uploaded")

# --- EXECUTE ---
if __name__ == "__main__":
    try:
        generate_and_upload()
        print("SUCCESS: Database populated!")
        print("Starting API...")
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        print(f"Error: {e}")
        print("Did you update the password in DATABASE_URL?")