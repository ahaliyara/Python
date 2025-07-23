# ▶️ Required Libraries
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine


# ▶️ Step 1: Connect to PostgreSQL (update with your credentials)
db_user = "postgres"
db_pass = "vnp-1234"
db_host = "localhost"
db_port = "5432"
db_name = "Foodr"

engine = create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}")
print("✅ Connected to the database successfully!")
# ▶️ Step 2: Load tables into Pandas DataFrames


meals_df = pd.read_sql("SELECT * FROM meals", engine)
orders_df = pd.read_sql("SELECT * FROM orders", engine)
stock_df = pd.read_sql("SELECT * FROM stock", engine)
print("\nSample meals data:")
print(meals_df.head())
print("\nSample orders data:")
print(orders_df.head())
print("\nSample stock data:")
print(stock_df.head())
