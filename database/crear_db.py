import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv("credenciales.env")

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS sars_mexico")
print("Base de datos 'sars_mexico' creada.")
cursor.close()
conn.close()