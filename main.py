import pandas as pd
import sqlite3

# Load CSV into DataFrame
df = pd.read_csv("data/pgadata.csv")

# Connect to SQLite (will create if it doesn't exist)
conn = sqlite3.connect("golf.db")

# Write to SQL table
df.to_sql("pga_tournaments", conn, if_exists="replace", index=False)

# Preview 5 rows
print(pd.read_sql("SELECT * FROM pga_tournaments LIMIT 5;", conn))

conn.close()
