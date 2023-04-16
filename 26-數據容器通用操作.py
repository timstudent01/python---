# len(容器)

# max(容器)

# min(容器)
mylist = [1,2,3]
mytuple = (1,2,3,4,5)
mystr = "itheima"

print(max(mylist))
print(max(mytuple))
print(max(mystr))

print(min(mylist))
print(min(mytuple))
print(min(mystr))

print(len(mylist))
print(len(mytuple))
print(len(mystr))

# alt+shift+拖動鼠標可以一次選個地方

# 通用類型轉換 (字典都會丟失 value)

#   list(容器)
#   tuple(容器)
#   str(容器)
#   set(容器)

# 但是不能轉字典，因缺乏鍵值對

# sorted(容器) 可以排序，由小到大，但是會變成列表
mytuple2 = (3333,434,7,45,4,44,213)
print(sorted(mytuple2))
# sorted(容器,reverse = True) 反轉順序，默認為False
print(sorted(mytuple2,reverse = True))
