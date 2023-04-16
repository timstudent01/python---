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


    
