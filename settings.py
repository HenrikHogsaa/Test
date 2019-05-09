import os



# DATABASE_URI = "postgresql://perenna:perenna@localhost/perenna" #Daniel
# DATABASE_URI = "mssql+pyodbc://PaulS:Perenna01@DESKTOP-V2HKR22\SQLEXPRESS/PbPrototype?driver=ODBC+Driver+17+for+SQL+Server" #Paul Laptop
# DATABASE_URI = "mssql+pyodbc://PaulS:Perenna01@./PbPrototype?driver=ODBC+Driver+17+for+SQL+Server" #Paul Perenna Office
DATABASE_URI = "mssql+pyodbc://Paul:Perenna01@localhost:1433/PbPrototype?driver=ODBC+Driver+17+for+SQL+Server" #Paul Home

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
