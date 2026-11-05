
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True
print("Primes below 50:", end=" ")
for n in range(2, 50):
    if is_prime(n):
        print(n, end=" ")
print()
count = 0
for n in range(2, 100):
    if is_prime(n):
        count += 1
print("Number of primes below 100:", count)
def goldbach(n):
    for p in range(2, n):
        q = n - p
        if is_prime(p) and is_prime(q):
            return (p, q)
    return None
for n in range(4, 31, 2):
    p, q = goldbach(n)
    print(n, "=", p, "+", q)
holds = True
for n in range(4, 10001, 2):
    if goldbach(n) is None:
        holds = False
        break
print("Goldbach holds for every even number from 4 to 10000:", holds)
