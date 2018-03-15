def num(s, k):
    # 统计字符串中字符出现次数排序倒数第k个字符
    dict1 = {}
    dict2 = {}
    nums = []
    for i in s:
        if i in dict1:
            continue
        else:
            dict1[i] = s.count(i)
    print(dict1)
    for key, value in dict1.items():
        if value not in dict2:
            nums.append(value)
            dict2[value] = []
            dict2[value].append(key)
        else:
            if key in dict2[value]:
                continue
            else:
                dict2[value].append(key)
    print(dict2)
    nums.sort()
    n = len(nums)
    # k = nums[n - k]
    nums.reverse()
    print(nums)
    k = nums[k - 1]
    print(k)
    return dict2[k]
if __name__ == "__main__":
    s = "lujfouowofkshklf"
    k = 3
    print(num(s, k))
