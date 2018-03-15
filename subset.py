def subset(nums):
    res = [[]]
    for num in sorted(nums):
        res += [item + [num] for item in res]
    return res


if __name__ == '__main__':
    dict = {}
    nums = []
    list = ["北京", "今天", "天气", "怎么样"]
    for i in range(len(list)):
        dict[i] = list[i]
        nums.append(i)
    print(dict)
    result = subset(nums)
    for items in result:
        res = []
        if len(items) == 0:
            continue
        for item in items:
            res.append(dict[item])
        print(res)
