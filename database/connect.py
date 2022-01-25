import pyodbc

conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=LAPTOP-F7505P7R\MSSQLSERVER01;'
    r'DATABASE=User;'
    r'Trusted_Connection=yes;'
)
sqlDbconn = pyodbc.connect(conn_str)