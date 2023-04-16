

# 定義集合
# 內容無序，且去重複性
my_set = {"傳智黑馬","黑馬程序員","itheima","傳智黑馬","黑馬程序員","itheima","傳智黑馬","黑馬程序員","itheima"}
my_set2 = {"傳智教育","黑馬程序員","itheima","傳智教育","黑馬程序員","itheima","傳智教育","黑馬程序員","itheima"}
my_set_empty = set()

print(f'my_set的內容是 : {my_set},類型是 :{type(my_set)}')
print(f'my_set2的內容是 : {my_set2},類型是 :{type(my_set2)}')
print(f'my_set_empty的內容是 : {my_set_empty},類型是 :{type(my_set_empty)}')

# 因為無序，所以不支持下標索引訪問，但是允許修改

# 添加新元素
# 語法: 集合.add(元素)。將指定元素，加到集合內。
# 結果: 集合本身被修改，添加了新元素

my_set.add("我超帥")
print(my_set)

# 移除元素
# 語法: 集合.remove(元素)。將指定元素移除。
my_set.remove("黑馬程序員")
print(my_set)

# 隨機取出一個元素 集合.pop()
element = my_set.pop()
print(f'被取出的元素是　: {element}')

# 清空集合 集合.clear()

my_set.clear()

print(my_set)

# 取兩個集合的差集 
# 語法: 集合1.difference(集合2) 
# 功能: 顯示1有2沒有的

set1 = {1,2,3,7,8}
set2 = {1,2,3,4,5,6}

print(set1.difference(set2)) # 7,8
print(set2.difference(set1)) # 4,5,6

# 消除兩個集合的交集
# 語法: 集合1.difference_update(集合2) 
# 功能: 在 集合1 裡面刪除和 集合2 相同的元素。
# 結果: 集合1 被修改，集合2 不變

set1.difference_update(set2)

print(set1)
print(set2)

# 將兩個集合結合
# 語法: 集合1.union(集合2)

set3 = set1.union(set2)

print(set3)

# 統計集合的元素數量 len()
print(len(set3))

# 集合的遍歷 
# 不支持下標索引，所以不能用while循環

for x in set3:
    print(x)


# 課後練習

#  my_list3=['黑馬程序員','傳智播客','itheima','傳智播客','傳智播客','itheima','黑馬程序員','itheima','itheima']

# 1. 定義一個空集合
myset = set()

# 2. for遍歷
# 3. 加到集合
my_list3 = ['黑馬程序員','傳智播客','itheima','傳智播客','傳智播客','itheima','黑馬程序員','itheima','itheima']

for x in my_list3:
    myset.add(x)

# 4. 打印集合
print(myset)