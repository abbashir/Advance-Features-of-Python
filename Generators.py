def topten():
    n = 1
    while n <= 10:
        sq = n * n
        n += 1
        yield sq


values = topten()
print(next(values))
print(next(values))
print(next(values))
print('He')
for i in values:
    print(i)
