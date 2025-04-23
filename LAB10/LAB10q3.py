def generate_odd_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        ni, nj = (i - 1) % n, (j + 1) % n
        if magic_square[ni][nj]:
            i = (i + 1) % n
        else:
            i, j = ni, nj
    return magic_square

def generate_doubly_even_magic_square(n):
    magic_square = [[(n*y)+x+1 for x in range(n)] for y in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3):
                magic_square[i][j] = n*n - (n*i + j)
    return magic_square

def generate_singly_even_magic_square(n):
    half = n // 2
    sub_square = generate_odd_magic_square(half)
    magic_square = [[0]*n for _ in range(n)]
    for i in range(half):
        for j in range(half):
            magic_square[i][j] = sub_square[i][j]
            magic_square[i + half][j] = sub_square[i][j] + 2 * half * half
            magic_square[i][j + half] = sub_square[i][j] + 3 * half * half
            magic_square[i + half][j + half] = sub_square[i][j] + half * half
    k = (n - 2) // 4
    for i in range(n):
        for j in range(n):
            if i < half:
                if j < k or j >= n - k:
                    if j < half:
                        magic_square[i][j], magic_square[i + half][j] = magic_square[i + half][j], magic_square[i][j]
            elif i == half:
                if j == k:
                    magic_square[i][j], magic_square[i - half][j] = magic_square[i - half][j], magic_square[i][j]
    return magic_square

def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

sizes = [4, 5, 6, 7, 8]
squares = {n: generate_magic_square(n) for n in sizes}

for n in sizes:
    print(f"Magic Square of size {n}:")
    for row in squares[n]:
        print(row)
    print()
