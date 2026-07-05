import pyodbc
import pandas as pd

connection_string = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=AISHAMADIYAH\\SQLEXPRESS;"
    "Database=CreditRiskDB;"
    "Trusted_Connection=yes;"
) #contains the info that python needs to find & log into my SQL server

connection = pyodbc.connect(connection_string) #actually does the opeining of the connection using prior info

query = "select * from credit_applications"
df = pd.read_sql(query, connection) #runs the query and stores the result in a pandas dataframe
df = df.drop(columns=["column1"])


print(df.head())
print("Shape:", df.shape)

print(df.info()) #gives me a summary of the df