import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper = s.str.upper()
lower = s.str.lower()
lengths = s.str.len()

result = pd.concat([upper, lower, lengths], axis=1, keys=['Uppercase', 'Lowercase', 'Length'])
print(result)