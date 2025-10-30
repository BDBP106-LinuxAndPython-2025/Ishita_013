#!/usr/bin/python3

import pandas as pd

# Load dataset
df = pd.read_csv('diabetes.csv')
# Print column names
print("Column names in the DataFrame:", df.columns)
print()


# ii print the first 10 rows
print("First 10 rows of the DataFrame:", df.head(10))
print()

# iii print the mean of the bloodpressure values
print("Mean BloodPressure value:", df['BloodPressure'].mean())
print()


# iv. print the first 4 rows of columns 3,4,5
# Note: Columns are zero-indexed.
cols = df.columns[[2, 3, 4]]  # 3rd, 4th, 5th columns
print("First 4 rows of columns 3, 4, 5:", df.loc[:3, cols])  # Rows 0 to 3 (first 4 rows)
print()

#Add 'NormalizedBP' column using min-max normalization
min_bp = df['BloodPressure'].min()
max_bp = df['BloodPressure'].max()
df['NormalizedBP'] = (df['BloodPressure'] - min_bp) / (max_bp - min_bp)
print("Added NormalizedBP column using min-max normalization.", df[['BloodPressure', 'NormalizedBP']].head())
# Show first few rows for check
print()

# vi  Create a function categorize_age to add the age category column
def categorize_age(age):
    if age <= 18:
        return "Youth"
    elif age <= 50:
        return "Adult"
    else:
        return "Senior"

df['age_category'] = df['Age'].apply(categorize_age)
print("Added age_category column based on age brackets." , df['age_category'])


