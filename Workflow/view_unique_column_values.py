import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from Utils.ExtractDatasetColumnOptions import extract_dataset_column_options

# Datasets
original_flights_ds = './DataSets/flights_2024-2025.csv'

# Extract key, values of the dataset
column_values = extract_dataset_column_options(original_flights_ds)
print(column_values)

# Transform column value in a dataframe managing cases where columns data are not the same lenght
df = pd.DataFrame([
    {'Column':k, 'Values':v}
    for k, v in column_values.items()
])

# Remove row where in 'Column' column we have 'Results'
# df = df[df['Column'] != 'Results'] 
df.drop(df[df['Column'] == 'Results'].index, inplace=True) # In-place
print(df)