# 普通的字符串split
str = "how is the weather today ?"
list1 = str.split()
list1.reverse()
string = ' '.join(list1)
print("普通的字符串split：" + '\n' + string)

# 人工将字符串转化成列表，然后再倒序
str = "how is the weather today ?"
list2 = []
start = 0
end = 0
for i in range(0, len(str)):
    if i == len(str) - 1:
        list2.append(str[start:])
    elif str[i] == ' ':
        end = i
        list2.append(str[start: end])
        start = i + 1
    else:
        end += 1
list2.reverse()
string = ' '.join(list2)
print("人工将字符串转化成列表，然后再倒序: " + "\n" + string)

# 先将整个字符串逆序，然后再将词反转回来
str = "how is the weather today ?"
str = str[::-1]
start, end = 0, 0
for i in range(len(str)):
    if i == len(str) - 1:
        tmp = str[start:]
        tmp = tmp[::-1]
        str = str.replace(str[start:], tmp)
    elif str[i] == ' ':
        end = i
        tmp = str[start:end]
        tmp = tmp[::-1]
        str = str.replace(str[start: end], tmp)
        start = i + 1
    else:
        end += 1
print("先将整个字符串逆序，然后再将词反转回来: " + '\n' + str)

# 使用正则split
import re

str = "how is the weather today ?"
result = re.split(r'(\s+)', str)
result.reverse()
result = ''.join(result)
print("使用正则split: " + '\n' + result)
