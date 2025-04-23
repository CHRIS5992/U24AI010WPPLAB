import pandas as pd
from datetime import datetime, date, time

a = pd.Timestamp('2012-01-15')
b = pd.Timestamp('2023-01-01 21:20:00')
c = pd.Timestamp.now()
d = pd.Timestamp('2023-04-23').date()
e = pd.to_datetime('today').date()
f = pd.Timestamp.now().time()
g = datetime.now().time()

print("a)", a)
print("b)", b)
print("c)", c)
print("d)", d)
print("e)", e)
print("f)", f)
print("g)", g)
