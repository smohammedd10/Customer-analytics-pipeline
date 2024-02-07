import pandas as pd
import json
import sqlite3

#Connect to database
conn = sqlite3.connect('customer.db')
#Extract data
query = "SELECT* FROM customers"
data = pd.read_sql(query, conn)
#Save data to csv
data.to_csv('customer_data.csv', index=False)
#Close the database connection
conn.close()

