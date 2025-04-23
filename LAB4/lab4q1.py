def min_operations_to_palindrome(s: str) -> int:
    operations = 0
    n = len(s)
    
    for i in range(n // 2):
        operations += abs(ord(s[i]) - ord(s[n - i - 1]))
    return operations


T = int(input("Enter number of test cases: "))
results = []

for _ in range(T):
    s = input().strip()
    results.append(str(min_operations_to_palindrome(s)))


print("\n".join(results))
