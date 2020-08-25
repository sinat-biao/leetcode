# 删除重复元素
a = ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't'] 
b = {}
# 1.先统计每个元素出现的次数
for i in a:
    if i in b.keys():
        b[i] = b[i] + 1
    else:
        b[i] = 1
print(b)
# 2.删除出现次数大于1的第一个元素
for key, value in b.items():
    if value > 1:
        while value > 1:
            a.remove(key)
            value = value - 1
print(a)