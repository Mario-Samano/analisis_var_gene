import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv("credenciales.env")

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="sars_mexico"
)
cursor = conn.cursor()

with open("schema.sql") as f:
    for statement in f.read().split(";"):
        if statement.strip():
            cursor.execute(statement)

conn.commit()
cursor.close()
conn.close()
print("Tablas creadas.")