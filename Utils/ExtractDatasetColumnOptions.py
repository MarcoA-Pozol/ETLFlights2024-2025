import pandas as pd

def extract_dataset_column_options(filepath:str) -> dict:
    """
        Extract unique values from non-numeric columns and store their pair key, values as a list in a dict.
    """
    # Load dataset in a dataframe
    try:
        df = pd.read_csv(filepath)
    except:
        df = pd.read_excel(filepath)

    # Create a dict 
    unique_values = {
        col: df[col].dropna().unique().tolist()
        for col in df.select_dtypes(exclude=['number']).columns
    }
    return unique_values