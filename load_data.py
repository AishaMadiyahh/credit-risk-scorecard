import pyodbc
import pandas as pd

connection_string = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=AISHAMADIYAH\\SQLEXPRESS;"
    "Database=CreditRiskDB;"
    "Trusted_Connection=yes;"
)

connection = pyodbc.connect(connection_string)

query = "select * from credit_applications"
df = pd.read_sql(query, connection)

print(df.head())
print("Shape:", df.shape)