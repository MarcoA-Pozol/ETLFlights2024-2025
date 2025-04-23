import pandas as pd

def get_fuel_type_dataframe():
    """
        Retrieve a simple short but descriptive dataframe with most common fuel types used in domestic and international flights.
    """
    data= {
        'Fuel Type':['Jet A', 'Jet A-1', 'SAF'],
        'Used In':['Domestic', 'International', 'Mixed w/ Jet A/Jet A-1'],
        'Region':['Mainly U.S.', 'Global', 'Global (emerging)'],
        'Aircraft Type':['Commercial jets', 'Commercial jets', 'Commercial jets (certified models)']
    }
    df = pd.DataFrame(data=data)
    return df

print(get_fuel_type_dataframe())