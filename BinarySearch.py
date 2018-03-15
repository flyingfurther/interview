def BinarySearch(array, value):
    '''
    二分查找:
    :param array: 输入为一个排好序的数组
    :param value: 需要参与比较的数值
    :return: 如果数组array中存在数值value,直接返回value;如果不存在value，我们返回距离value最近的值并返回其下标
    '''
    low = 0
    height = len(array) - 1
    while low < height:
        mid = (low + height) // 2
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            height = mid - 1
        else:
            return array[mid], mid
    result, index = nearestValue(array, value, low)
    return result, index


def nearestValue(array, value, index):
    a = value - array[index - 1]
    b = array[index] - value
    if min(a, b) == a:
        result = array[index - 1]
    else:
        result = array[index]
    index = array.index(result)
    return result, index


if __name__ == "__main__":
    print(BinarySearch([1, 2, 3, 34, 56, 57, 78, 87], 77))
