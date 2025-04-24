import pandas as pd

# Pivot table from xls as df
df = pd.read_excel('./DataSets/flights_2025.xls')
df_ptable = pd.pivot_table(data=df, index='Airline', columns='Flight Type', values='Distance (km)', aggfunc='mean')
                           
print(df_ptable.fillna(0).round(2))

# Visualize pivot table data in a chart
import matplotlib.pyplot as plt

df_ptable.plot(kind='bar', figsize=(12, 6))
plt.title('Average Distance by Airline and Flight Type')
plt.ylabel('Distance (km)')
plt.xlabel('Airline')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Flight Type')
plt.tight_layout()
plt.show()

df_ptable.drop(columns='Total Avg', errors='ignore').plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Average Distance (Stacked) by Airline')
plt.ylabel('Distance (km)')
plt.xlabel('Airline')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Flight Type')
plt.tight_layout()
plt.show()

import seaborn as sns

sns.heatmap(df_ptable.drop(columns='Total Avg', errors='ignore'), annot=True, fmt=".0f", cmap="Blues")
plt.title('Heatmap of Average Distance by Airline and Flight Type')
plt.ylabel('Airline')
plt.xlabel('Flight Type')
plt.tight_layout()
plt.show()

df_ptable[['Domestic', 'International']].plot(kind='barh', figsize=(12, 10))
plt.title('Average Distance by Airline (Horizontal)')
plt.xlabel('Distance (km)')
plt.ylabel('Airline')
plt.tight_layout()
plt.show()