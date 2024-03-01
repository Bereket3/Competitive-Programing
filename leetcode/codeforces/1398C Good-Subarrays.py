from collections import Counter


for _ in range(int(input())):
    n = int(input())
    a = input()

    c = Counter()
    c[0] = 1

    out, pri = 0, 0

    for i in range(n):
        pri += int(a[i])
        x = pri - i - 1
        c[x] += 1
        out += c[x] - 1

    print(out)