# Ext_1 编写一个递归函数来计算列表包含的元素数。

def count(list):
    if list == []:
        return 0
    else:
        list = list[1:]
        summ = 1+ count(list)
    return summ
b=count([1,2,3,4])
print(b)
