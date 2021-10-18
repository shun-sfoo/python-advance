# 杨辉三角
def triple():
    L = [1]
    while True:
        yield L
        L = L + [0]  # 给每一行添加一个空位
        L = [L[i] + L[i - 1] for i in range(len(L))]


n = 0
results = []
for t in triple():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)
