import pandas as pd
import os

def transform_xls_to_csv(input_path: str, output_path: str = None):
    """
    Parse a xls/xlsx file to csv.
    
    Parameters:
    - input_path (str): Path to the input Excel file.
    - output_path (str): Path to save the output CSV file. If None, uses the input filename with .csv extension.
    
    Returns:
    - str: Path to the saved CSV file.
    """
    try:
        if not input_path.lower().endswith(('.xls', '.xlsx')):
            raise ValueError("Input file must have a .xls or .xlsx extension")

        df = pd.read_excel(input_path)

        if not output_path:
            output_path = os.path.splitext(input_path)[0] + '.csv'
        elif not output_path.lower().endswith('.csv'):
            output_path += '.csv'

        df.to_csv(output_path, index=False)
        return output_path
    except Exception as e:
        print(f"Error transforming Excel to CSV: {e}")
        return None


def transform_csv_to_xls(input_path: str, output_path: str = None):
    """
    Parse a csv file to xls/xlsx.
    
    Parameters:
    - input_path (str): Path to the input CSV file.
    - output_path (str): Path to save the output Excel file. If None, uses the input filename with .xlsx extension.
    
    Returns:
    - str: Path to the saved Excel file.
    """
    try:
        if not input_path.lower().endswith('.csv'):
            raise ValueError("Input file must have a .csv extension")

        df = pd.read_csv(input_path)

        if not output_path:
            output_path = os.path.splitext(input_path)[0] + '.xlsx'
        elif not output_path.lower().endswith(('.xls', '.xlsx')):
            output_path += '.xlsx'

        df.to_excel(output_path, index=False)
        return output_path
    except Exception as e:
        print(f"Error transforming CSV to Excel: {e}")
        return None
