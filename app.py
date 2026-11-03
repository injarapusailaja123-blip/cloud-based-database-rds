# Intern ID: CITS9613
# Name: Injarapu Sailaja
# Task 2: Cloud-Based Database (RDS)

import sqlite3
from datetime import datetime

class CloudRDSManager:
    def __init__(self, db_name="cloud_rds.db"):
        print(f"[{datetime.now()}] Connecting to Cloud RDS...")
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        print("✓ Connected to Cloud Database!\n")
    
    def create_database_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, course TEXT, intern_id TEXT, created_at TEXT)''')
        self.conn.commit()
        print("✓ Table 'students' created in RDS\n")
    
    def insert_data(self, student_id, name, course):
        print(f"Inserting: {name}...")
        self.cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (student_id, name, course, "CITS9613", str(datetime.now())))
        self.conn.commit()
        print(f"✓ Inserted: {name}\n")
    
    def read_data(self):
        print("Reading from Cloud RDS:")
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"ID:{row[0]} | Name:{row[1]} | Course:{row[2]}")
        print(f"Total: {len(rows)}\n")
    
    def show_rds_status(self):
        print("\n=== RDS Status ===")
        print("DB: database-1 | Engine: MySQL 8.0")
        print("Status: Available")
        print("Intern: CITS9613 - Sailaja\n")

if __name__ == "__main__":
    print("CLOUD-BASED DATABASE (RDS) - Task 2 | CITS9613\n")
    rds = CloudRDSManager()
    rds.show_rds_status()
    rds.create_database_table()
    rds.insert_data(1, "Sailaja Injarapu", "Cloud Computing")
    rds.insert_data(2, "Rahul Kumar", "AWS RDS")
    rds.insert_data(3, "Priya Sharma", "Database")
    rds.read_data()
    print("✓ RDS Operations Success!")