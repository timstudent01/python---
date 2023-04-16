for x in [35,72,73] :
    print((x+7/2))

# 1. 列表的查詢功能(方法)

# 功能: 查找指定的元素在列表的下標，找不到則報錯: ValueError
# 語法: 列表 index (元素)

# 2. index 就是列表對象 (變量) 內置的方法 (函數)
# 方法的操作及調用

class Student :
    def add(self,x,y):
        return x + y 

student = Student()
num = student.add


mylist =["itcast","itheima","python"]
print(mylist)

index = mylist.index("itheima")

print(f"itheima 在列表中的下標索引是: {index}")




# 3. 插入單個元素 .insert(位置,數據) 追加元素到列表尾部 .append() 

mylist.insert(1,"我超帥")

index = mylist.index("我超帥")

print(mylist)

print(f"我超帥 在列表中的下標索引是: {index}")

mylist[0:2] = "ㄏㄏ","耶耶"

print(mylist)

mylist.insert(4,"我超帥")

print(mylist)




# 4. 插入多個
# 語法: 列表.extend(其他數據容器)，依次追加到列表尾部。
mylist2 = [777,888,999]
mylist.extend(mylist2)

print(mylist)


# 5. 元素的刪除: del
# 語法1 : del 列表[下標]
# 語法2 : 列表.pop(下標) 可以刪除，甚至作為返回值，變量接收。

del mylist[3:5]
print(mylist)



element = mylist.pop(3)

print(f"通過pop方法取出元素後列表內容為 : {mylist},取出的元素為 : {element}")


# 6. remove刪除某元素在列表中的第一個匹配項，第一個元素刪掉，只能刪除一個。
# 語法: 列表.remove(元素)

mylist3 = [111,222,333,444,5555,66666]

print(mylist3)

mylist3.remove(333)

print(mylist3)

# 7. 清空列表
# 語法: 列表.clear()

mylist3.clear()

print(mylist3)

# 8. 統計列表中的某元素
# 語法: 列表.count(元素)
mylist4 = [111,222,333,444,5555,66666,111,111,111,222,111,111,111,111,111]
print(f"列表中111的數量是: {mylist4.count(111)}")

# 9. 統計列表中有幾個元素(長度)
# 語法: len(列表)
print(f"列表中總共有 {len(mylist4)} 個元素")