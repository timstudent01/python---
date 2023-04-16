# 定義字典變量
my_dict = {
    "周杰倫1":"趙承庭",
    "周杰倫2":"趙承庭2",
    "周杰倫3":"趙承庭3"
    }


# 定義空字典
my_dict2 = {}
my_dict3 = dict()

print(my_dict)
print(my_dict2)
print(my_dict3)

# 輸出 字典[""]
print(my_dict["周杰倫1"])
print(my_dict["周杰倫2"])
print(my_dict["周杰倫3"])

subject123 = {
    "王力宏":{
        "語文":77,
        "數學":66,
        "英語":33
        },
    "周杰倫":{
        "語文":88,
        "數學":86,
        "英語":55
        },
    "林俊傑":{
        "語文":99,
        "數學":96,
        "英語":66
        }
    }
print(subject123["王力宏"])
print(subject123["周杰倫"]["語文"])

# 新增元素
# 語法: 字典[key] = value
# 結果: 字典被修改，新增了元素

# 更新元素
# 語法: 字典[key] = value
# 注意: 字典key不可以重複，所以對已存在的key執行上述操作，就是更新value值

subject123["王力宏"]["語文"] = 0 
subject123["王力宏"]["化學"] = 90 
print(subject123["王力宏"])

# 刪除元素 字典.pop(key)
sub123 = subject123.pop("王力宏")

print(subject123)

print(sub123)

subject123["王力宏"]= sub123

print(subject123)

# 清空字典 字典.clear()



# 獲取全部的key
# 語法 : 字典.keys()
subkey = subject123.keys()
print(subkey)


# 遍歷 方式1 蒐集所有key

dict_a = {"我的興趣":"打手槍","我喜歡吃的食物":"肉燥飯","我的特色":"超帥"}

print(dict_a["我的興趣"])

dict_a_keys = dict_a.keys()

for h in dict_a_keys :
    print(f'{h}是 : {dict_a[h]} ')


# 遍歷 方式2 
for e in dict_a :
    print(e)
    print(dict_a[e])

# 統計字典內的元素數量 len(字典)
print(len(dict_a))
    

