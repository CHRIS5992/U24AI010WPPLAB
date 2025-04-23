import pandas as pd

# Sample DataFrame (replace with your actual data)
data = {
    'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
            'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday'],
    'john': [True, False, True, False, True, False, True, False, False, True],
    'judy': [False, True, True, False, True, True, False, False, True, True]
}
df = pd.DataFrame(data)

# Find party days (both John and Judy visiting)
df['party_day'] = df['john'] & df['judy']

# Calculate days until next party (in reverse order)
df['days_til_party'] = df.loc[::-1, 'party_day'].cumsum().sub(1).clip(lower=0)[::-1]

# Clean up - set 0 for actual party days and increment others
df['days_til_party'] = df.apply(
    lambda row: 0 if row['party_day'] else row['days_til_party'] + 1,
    axis=1
)

# Drop temporary column
df = df.drop(columns=['party_day'])

print(df)