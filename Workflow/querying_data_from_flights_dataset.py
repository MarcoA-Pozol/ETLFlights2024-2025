import pandas as pd

try:
    df = pd.read_csv('./DataSets/flights_2024-2025.csv')

    # Get Pilot names with the max and min total_revenue
    max_total_revenue_pilot_name = df[df['Total Revenue'] == df['Total Revenue'].max()]
    min_total_revenue_pilot_name = df[df['Total Revenue'] == df['Total Revenue'].min()]

    # Concatenate both results and drop duplicates if needed
    result = pd.concat([min_total_revenue_pilot_name, max_total_revenue_pilot_name]).drop_duplicates(subset='Pilot Name')
    
    
    result.reset_index()
    result.index = ['Min', 'Max']

    # Format pilot's name and revenues output
    result['Pilot Name'] = result['Pilot Name'].str.replace('Capt. ', '', regex=True) # Remove 'Capt.'
    result['Total Revenue'] = result['Total Revenue'].apply(lambda x: f'$ {x:,}')

    # Select only the Pilot Name and limit to 2 rows (Min and Max values in revenues)
    final_result = result[['Pilot Name', 'Total Revenue']].head(2)
    print(final_result)
    
    # Output
    #     |        Pilot Name | Total Revenue
    # -----------------------------------------
    # Min |       Sean Murphy |   $ -7,630.0
    # Max | Aisha Al-Mansoori |  $ 625,670.0
        
except Exception as e:
    print(f'Error while loading dataset: {e}')