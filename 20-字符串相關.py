


from dataclasses import replace


my_str = "itheima and itcast"

# 1. 通過下標索引取值

value = my_str[2]
value2 =my_str[-16]

print(value)
print(value2)

# 字符串跟元組一樣，是無法修改的容器

# 如果必須要做，只能得到新的字符串，老字符串無法修改

# 2. 查找內容

value3 = my_str.index("and")
print(value3)

# 3. 替換 replace 只能產生新字符串，原本的字符串沒變化

new_my_str = my_str.replace("it","程序")
my_str.replace("it","程序") # 無效
print(new_my_str)
print(my_str)

# 4. 字符串的分割
# 語法: 字符串.split(分隔符字符串)
# 功能: 按照指定的分隔符字符串，將字符串劃分為多個字符串，並存入列表對象中
# 注意: 字符串本身不變，而是得到了一個列表對象

str5 = "hello itheima itcast"
str5new = str5.split(" ") # 用空格隔開，也可以替換
print(str5)
print(str5new) # 得到的類型是列表

str6 = "我超帥真的帥無敵帥的啦"
str6new = str6.split("帥")
print(str6)
print(str6new)

# 5. 字符串的規整操作 strip() (去除前後的空格)
# 6. 字符串的規整操作 strip(字符串)
str7 = " 我超帥 嘿嘿 "
print(str7.strip())

str8 = "123 我超帥 嘿嘿 123"
print(str8.strip("12")) # 只去除前面12

str9 = "123 我超帥 嘿嘿 123"
print(str9.strip("123")) # 去除前後的123

# 7. 字符串出現的次數
print(str9.count("123"))

# 8. 統計字符串的長度
len(str9)

# 9.字符串遍歷

k = 0
while k < len(str9) :
    print(f"{k+1}.\t",str9[k])
    k+=1

for l in str9 :
    print(l)

# 10. 課題
# 給定一個字符串 "itheima itcast boxuegu"
str10 = "itheima itcast boxuegu"
# 統計字符串內有多少"it"字符
print(str10.count("it"))
# 將字符串中的空格修改成"|"字符
str11 = str10.replace(" ","|")
print(str11)
# 並按照"|"字符串分割，得到列表
str12 = str11.split("|")
print(str12)

