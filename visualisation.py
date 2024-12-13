# -*- coding: utf-8 -*-
"""visualisation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DWaVIjvfLjKg8iIjeDYF0bt5BTjf_UD6
"""

import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler, MinMaxScaler

"""# Load the dataset"""

file_path = '/content/cleaned_data.csv'
data_cleaned = pd.read_csv(file_path)

"""# Display original column names to identify the columns to rename"""

original_column_names = data_cleaned.columns.tolist()
print("Original Column Names:\n", original_column_names)

"""# Rename columns"""

data_cleaned.rename(columns={
    'ontime_departures_\n(%)': 'ontime_departures_(%)',
    'ontime_arrivals_\n(%)': 'ontime_arrivals_(%)',
    'cancellations_\n\n(%)': 'cancellations_(%)'
}, inplace=True)

"""# Display updated column names to verify renaming"""

updated_column_names = data_cleaned.columns.tolist()
print("Updated Column Names:\n", updated_column_names)

"""# Identify missing values"""

missing_values = data_cleaned.isnull().sum()
print("Missing values in each column:\n", missing_values)

"""# Fill missing values"""

for column in data_cleaned.columns:
    if data_cleaned[column].dtype == 'object':
        data_cleaned[column].fillna(data_cleaned[column].mode()[0], inplace=True)
    else:
        data_cleaned[column].fillna(data_cleaned[column].median(), inplace=True)

"""# Remove rows or columns with significant missing data if necessary"""

threshold = 0.6  # Remove columns with more than 60% missing values
data_cleaned.dropna(thresh=int(threshold * len(data_cleaned)), axis=1, inplace=True)
data_cleaned.dropna(inplace=True)

# Identify and remove duplicate rows

duplicates = data_cleaned.duplicated()
print(f"Number of duplicate rows: {duplicates.sum()}")
data_cleaned = data_cleaned.drop_duplicates()

"""# Using Z-score to detect outliers"""

z_scores = np.abs(stats.zscore(data_cleaned.select_dtypes(include=[np.number])))
outliers = (z_scores > 3).sum(axis=1)
print(f"Number of outliers: {(outliers > 0).sum()}")

"""# remove outliers"""

data_cleaned = data_cleaned[(z_scores < 3).all(axis=1)]

"""# Standardize data"""

scaler = StandardScaler()
data_standardized = pd.DataFrame(scaler.fit_transform(data_cleaned.select_dtypes(include=[np.number])), columns=data_cleaned.select_dtypes(include=[np.number]).columns)

"""# Normalize data"""

scaler = MinMaxScaler()
data_normalized = pd.DataFrame(scaler.fit_transform(data_cleaned.select_dtypes(include=[np.number])), columns=data_cleaned.select_dtypes(include=[np.number]).columns)

"""# Convert columns to appropriate data types"""

data_cleaned['Month'] = pd.to_datetime(data_cleaned['Month'], errors='coerce')

"""# Ensure categorical consistency"""

data_cleaned['Route'] = data_cleaned['Route'].str.strip().str.lower()

"""# Encoding categorical data"""

data_encoded = pd.get_dummies(data_cleaned, columns=['Route', 'Airline'], drop_first=True)

"""# Apply consistent formatting"""

data_cleaned.columns = data_cleaned.columns.str.strip().str.lower().str.replace(' ', '_')

"""# Display column names to identify irrelevant columns"""

column_names = data_cleaned.columns.tolist()
print("Column Names:\n", column_names)

"""# Aggregate data"""

data_aggregated = data_cleaned.groupby('month').agg({
    'sectors_flown': 'sum',
    'cancellations': 'sum',
    'departures_on_time': 'mean',
    'arrivals_on_time': 'mean'
}).reset_index()

"""# Transform data"""

data_aggregated['log_sectors_flown'] = np.log1p(data_aggregated['sectors_flown'])

"""# Create new features"""

data_cleaned['on_time_ratio'] = data_cleaned['departures_on_time'] / data_cleaned['arrivals_on_time']

"""# Automate checks"""

def validate_data(df):
    assert df.isnull().sum().sum() == 0, "There are missing values"
    assert df

"""#Downloading the cleaned dataset"""

import pandas as pd

# Save the cleaned and renamed dataset to a new CSV file
data_cleaned.to_csv('cleaned_data_final.csv', index=False)

from google.colab import files

# Download the file
files.download('cleaned_data_final.csv')