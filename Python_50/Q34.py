# Implement a generator to yield even numbers from 1 to n.
def even_gen(n):
    for i in range(2, n+1, 2):
        yield i
for e in even_gen(10):
    print(e)