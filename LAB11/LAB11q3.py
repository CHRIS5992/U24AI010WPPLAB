import pandas as pd

asking_prices = pd.Series([15000, 18000, 17000, 16000, 14000])
fair_prices = pd.Series([16000, 17500, 17500, 16500, 15000])

good_deals = asking_prices[asking_prices < fair_prices].index.tolist()

print(good_deals)
