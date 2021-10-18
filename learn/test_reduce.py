from functools import reduce


def fn(l):
    r = reduce(lambda x, y: (x * 10) + y, l)
    return r


digits = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def char2num(c):
    return digits[c]


def str2num(s):
    return reduce(lambda x, y: 10 * x + y, map(char2num, s))


print(str2num("13579"))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：


def normalize(name):
    first = name[0].upper()
    last = name[1:].lower()
    name = first + last
    return name


def normalize_simple(name):
    return name.title()


print(list(map(normalize, ["adam", "LISA", "barT"])))
print(list(map(normalize_simple, ["adam", "LISA", "barT"])))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    num = s.split(".")
    p1 = num[0]
    p2 = num[1]
    p2 = p2[::-1]
    r1 = reduce(lambda x, y: x * 10 + y, map(char2num, p1))
    r2 = reduce(lambda x, y: (x / 10) + y, map(char2num, p2))
    return r1 + (r2 / 10)


if abs(str2float("123.456") - 123.456) < 0.00001:
    print("测试成功!")
else:
    print("测试失败!")
