import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Utils.FilesParsing import transform_xls_to_csv
transform_xls_to_csv(input_path='./DataSets/flights_2024-2025.xls', output_path='./DataSets/flights_2024-2025.csv')