from itertools import product
with open("input1.txt", 'r') as f:
    A = list(map(int, f.readlines()))
    # A = [1, 2, 3, 4]
print(f'A = {A}')
res1 = [(i, j) for i, j in product(A, repeat=2) if i % j == 0]
res2 = [(i, j) for i, j in product(A, repeat=2) if i <= j]

print(f"The pair list for a/b: {res1}")
print(f"The pair list for a<=b: {res2}")
