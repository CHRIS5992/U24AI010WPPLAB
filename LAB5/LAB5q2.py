def max_chocolate_pieces(K):
    # Split the cuts into horizontal and vertical cuts as evenly as possible
    h = K // 2
    v = K - h
    # The maximum number of pieces is (h + 1) * (v + 1)
    return (h + 1) * (v + 1)
    
# Read the number of test cases
T = int(input())
# Read the K values for each test case
K_values = list(map(int, input().split()))
# Compute and print the result for each test case
for K in K_values:
    print(max_chocolate_pieces(K))