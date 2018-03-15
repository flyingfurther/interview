def keepTheBiggestValue(num, k):
    '''
    给定一个十进制的正整数num，选择从里面去掉k个数字，希望保留下来的数字组成的正整数最大。
    :param num: 十进制的正整数
    :param k: 从num中去掉的数字的个数
    :return: 返回最后的最大正整数
    '''
    string = str(num)
    stack, drop = [], 0
    for i, c in enumerate(string):
        while stack and c > stack[-1] and drop < k:
            # statck[-1] represents the top elements of the stack and also means the last one of the list.
            drop += 1
            stack.pop()
        stack.append(c)
    print(''.join(stack[:len(string) - k]))


if __name__ == "__main__":
    num1 = 325
    k1 = 1
    keepTheBiggestValue(num1, k1)

    num2 = 325167
    k2 = 3
    keepTheBiggestValue(num2, k2)
