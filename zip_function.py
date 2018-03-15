def f():
    x = {'age': 18, 'name': 'dh', 'id': 3306}
    for tuple in zip(x.values(), x.keys()): # zip返回的是元组
        yield tuple
    for res in zip(*zip(x.values(), x.keys())):
        yield res
    dictionary = dict(zip(x.values(), x.keys()))    # 使用zip将字典反转并转化成新的字典
    yield dictionary

if __name__ == '__main__':
    for result in f():
        print(result)
