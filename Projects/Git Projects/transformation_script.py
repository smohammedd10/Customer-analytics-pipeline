import pandas as pd

# Load the extracted data
data = pd.read_csv('customer_data.csv')
# Data cleaning and transformation
# (Add your transformation logic here)
# Calculate metrics
# (Add your metric calculations here)
# Save the transformed data
data.to_csv('transformed_customer_data.csv', index=False)