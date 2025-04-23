import pandas as pd
import numpy as np
from itertools import product

data = pd.DataFrame({
    'date': pd.to_datetime([
        '2023-01-15', '2023-01-20', '2023-02-15', '2023-01-15',
        '2023-02-20', '2023-03-10', '2023-02-15', '2023-03-20'
    ]),
    'artist': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'B'],
    'venue': ['X', 'Y', 'X', 'X', 'Y', 'Z', 'Y', 'Z']
})

artists = pd.Series(['A', 'B', 'C'])
venues = pd.Series(['X', 'Y', 'Z'])

data['year_month'] = data['date'].dt.to_period('M')
grouped = data.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')

all_combinations = pd.DataFrame(list(product(
    data['year_month'].unique(), artists, venues
)), columns=['year_month', 'artist', 'venue'])

merged = pd.merge(all_combinations, grouped, on=['year_month', 'artist', 'venue'], how='left')
merged['count'] = merged['count'].fillna(0).astype(int)

merged['column'] = merged['artist'] + '_' + merged['venue']
pivot = merged.pivot(index='year_month', columns='column', values='count').fillna(0).astype(int)

print(pivot)
