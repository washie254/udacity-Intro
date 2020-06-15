"""
Expected Output:
    [0, 1, 2, 3]
    [4, 5, 6, 7]
    [8, 9, 10, 11]
    [12, 13, 14, 15]
    [16, 17, 18, 19]
    [20, 21, 22, 23]
    [24]
"""
def chunker(iterable, size):
    # Implement function here
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))