
# 1. 定義列表，用變量接收他

mylist = [21,25,21,23,22,20]

# 2. 追加一個數字31到尾部
listadd = [31]

mylist.extend(listadd)

print(mylist)

# 3. 追加一個新列表[29,33,30] 到尾部
listadd2 = [29,33,30]

mylist.extend(listadd2)

print(mylist)

# 4. 取出第一個元素(應是:21)
unit1 = mylist.pop(0)
print(unit1)
print(mylist)

# 5. 取出最後一個元素(應是:30)
unit2 = mylist.pop(8) # 應該要取-1 因為不知道最後元素是第幾個位置
print(unit2)
print(mylist)

# 6. 查找元素31，在列表中的位置
index = mylist.index(31)
print(mylist)
print(index)
