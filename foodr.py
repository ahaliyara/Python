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

# ✅ Task 1: How many unique meals and eateries exist?
print("\n✅ Task 1: Unique counts")
print("Unique meals:", meals_df["meal_id"].nunique())
print("Unique eateries:", meals_df["eatery"].nunique())

# ▶️ Step 3: Total revenue per meal
orders_df["order_revenue"] = orders_df["order_quantity"] * orders_df["meal_id"].map(
   meals_df.set_index("meal_id")["meal_price"]
)
revenue_per_meal = orders_df.groupby("meal_id")["order_revenue"].sum().reset_index()
revenue_per_meal = revenue_per_meal.merge(meals_df[["meal_id", "eatery"]], on="meal_id", how="left")
print("\n✅ Task 2: Top 5 revenue-generating meals:")
print(revenue_per_meal.sort_values(by="order_revenue", ascending=False).head())