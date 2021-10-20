# 生成素数集合

## 第一步生成所有的奇数, 从 3 开始
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


## 排除可以整除奇数的序列
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2  # 第一个数是2
    it = _odd_iter()  # 拿到从 3 开始的奇数集合
    while True:
        n = next(it)  # 指向下一个 （排除了某数集合的下一个）
        yield n
        it = filter(_not_divisible(n), it)  # 从集合中排除掉 n ,够成没有n倍数的新集合，返回该集合参与下一次运算


# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break
