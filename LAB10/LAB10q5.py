import numpy as np

arr = np.array(['apple', 'banana', 'cherry', 'date'])

centered = np.char.center(arr, 15, fillchar='_')
left_justified = np.char.ljust(arr, 15, fillchar='_')
right_justified = np.char.rjust(arr, 15, fillchar='_')

print("Centered:\n", centered)
print("Left-justified:\n", left_justified)
print("Right-justified:\n", right_justified)
