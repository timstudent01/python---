

# 1. 元組定義 : 定議元組使用小括號，且使用逗點隔開各個數據，數據可以是不同的數據類型。

# 2. 定義元組字面量 : 

from email.headerregistry import ContentTransferEncodingHeader


t1 = (1,2,3,4,5,6,7)

# 3. 定義空元組 :

t2 = ()         # 方式 1

t3 = tuple()    # 方式 2 類對象

print(t1,t2,t3)

# 4. 定義 1個 元素的元組 : 

t4 = (17,) # 後面一定要有逗點，否則不會成為元組類型。

# 5. 用下標索引取出元組元素 : 

t5 = ((5,7,8),(9,2,4))
print(t5[0][2])

# 6. 元組的相關操作 :

    # a. index()
t6 = (7,8,9,7,8,5,6,7)

print(t6.index(8))

    # b. count()
print(t6.count(8))

    # c. len(元組)
print(len(t6))

#  7. 元組的 while 遍歷 :

c = 0
while c < len(t6) :
    d = t6[c]
    print(d)
    c+=1


#  8. 元組的 for 遍歷 :
def func_e():
    for e in t6 :
        print(e)

func_e()


# 9. 不可修改 元組內容，但是可以修改 元組裡面的 列表內容 : 

t7 = ((1,2,3),[7,8,9])
print(t7)

t7[1][2] = 10
print(t7)

del t7[1][2]
print(t7)

t7 [1][2:4] = [11,12]
print(t7)

# 10. 元組課題 :
# 定義一個元組，內容是('周杰倫',11,['football','music'])，紀錄的是一個學生的姓名、年齡、愛好
# 請透過元組的功能，對其進行 :

g = (('周杰倫',11),['football','music'])

# 1. 查詢其年齡所在的下標位置

h = g[0].index(11)
print(h)

# 2. 查詢學生的姓名

i = g[0].index('周杰倫')
# 3. 刪除學生愛好中的football

del g[1][0]

print(g)
# 4. 增加愛好: coding 到愛好list內

g[1].append("coding")

print(g)

