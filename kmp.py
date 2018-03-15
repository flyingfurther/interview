# 得到局部匹配值PMT的数组，并生成对应的next数组
def getnext(a, next):
    al = len(a)
    next[0] = -1
    k = -1
    j = 0
    while j < al - 1:
        if k == -1 or a[j] == a[k]:
            j += 1
            k += 1
            next[j] = k
        else:
            k = next[k]


def KmpSearch(a, b):
    i = j = 0
    al = len(a)
    bl = len(b)
    while i < al and j < bl:
        if j == -1 or a[i] == b[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == bl:
        return i - j
    else:
        return -1


if __name__ == '__main__':
    a = 'ABABCABDABBGAFDSBVSABDABB'
    b = 'ABDABB'
    next = [0] * len(b)  # 长度为len(b)的列表
    print(next)
    getnext(b, next)
    t = KmpSearch(a, b)
    print(next)
    print(t)