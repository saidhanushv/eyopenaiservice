import pyodbc

server = 'saidhanushserver.database.windows.net'
database = 'saidhanushdatabase007'
username = 'saidhanushserver'
password = 'Aizen101'

# Connection string
driver = '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
)

cursor = cnxn.cursor()
cursor.close()
cnxn.close()