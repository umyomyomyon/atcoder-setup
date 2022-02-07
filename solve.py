h, w = map(int, input().split())
a = []
for i in range(h):
    b = list(map(int, input().split()))
    a.append(b)

ans = [[0 for _ in range(h)] for _ in range(w)]
for i in range(h):
    for j in range(w):
        ans[j][i] = a[i][j]

for i in range(w):
    for j in range(h):
        print(ans[i][j], end=" ")
    print()
