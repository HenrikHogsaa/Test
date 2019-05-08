import os

# DATABASE_URI = "postgresql://perenna:perenna@localhost/perenna"
DATABASE_URI = "mssql+pyodbc://PaulS:Perenna01@localhost:1433/PbPrototype?driver=ODBC+Driver+17+for+SQL+Server"

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
