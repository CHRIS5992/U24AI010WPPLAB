student_names = []

print("Enter the names of 10 students:")

for i in range(10):
    name = input(f"Student {i + 1}: ")
    name = name[:15]
    student_names.append(name)

print("\nReversed Student Names:")
for name in student_names:
    print(name[::-1])
