n, k = input().split(' ')
n = int(n)
k = int(k)


def combinations(n, k):
    if k > n:
        return 0
    if n == k or k == 0:
        return 1
    else:
        return combinations(n-1, k-1) + combinations(n-1, k)
print(combinations(n, k))
