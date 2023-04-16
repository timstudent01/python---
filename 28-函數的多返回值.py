
from ast import keyword
from telnetlib import PRAGMA_HEARTBEAT


def test_return():
    return 1,2

x,y = test_return()

print(x)
print(y)


# 函數參數種類

# 1. 位置參數
def user_info(name,age,gender) :
    print(f"你的名字是{name}，年齡是{age}，性別是{gender}")

user_info ("TOM",20,"男")

# 注意: 傳遞的參數和定義的參數順序及個數必須一致。


# 2. 關鍵字參數
def user_info2(name,age,gender):
    print(f"您的名字是: {name},年齡是: {age},性別是: {gender}")

user_info2(name="小明",age=20,gender="男")  
# 可以不按照固定順序  
user_info2(name="小明",gender="男",age=20)
# 可以和位置參數混用，位置參數必須在前，且匹配參數順序。 
user_info2("小明",age=20,gender="男")
    
# 注意: 函數調用時，如果有位置參數時，位置參數必須在關鍵字參數的前面，但關鍵字參數之間不存在先後順序。

# 3. 缺省參數
# 缺省參數也可以叫作"默認參數"，用於定義函數，為參數提供默認值，調用函數時可不傳該默認參數的值
# (注意: 所有位置參數必須出現在默認參數前，包含函數定義和調用)

# 作用: 當調用函數時沒有傳遞參數，就會使用默認使用缺省參數對應的值。
def user_info3(name,age,gender="男") :
    print(f"您的名字是: {name},年齡是: {age},性別是: {gender}")


user_info3("TOM",20)
user_info3("Rose",18,"女")
# 注意: 函數調用時，如果為缺省參數傳值，則修改默認參數值，否則使用這個默認值。

# 若是前面的默認值要生效，其後的一個默認值一定要設定，否則報錯。

def user_info4(name,age=12,gender="女") :
    print(f"您的名字是: {name},年齡是: {age},性別是: {gender}")
user_info4("Rose2",18,"女")

# 4. 不定長參數
# 不定長參數也叫"可變參數"，用於不確定調用的時候會傳遞多少個參數(不傳參也可以)的場景。
# 作用: 當調用函數時不確定參數個數時，可以使用不定長參數。

# 不定長參數的類型:
# (1.) 位置傳遞
# (2.) 關鍵字傳遞

def user_info5 (*args): # 標註* 表示可以傳送無限參數
    print(args) # 所有參數被args蒐集，根據參數"傳遞的位置"成為一個元組(tuple)

# (1.) 位置傳遞 不定長 1個星號
user_info5("Tom",18,992)    
user_info5(930902,"rose",3323,False)

# (2.) 關鍵字傳遞 不定長 2個星號
def user_info6 (**kwargs): # 標註** 表示可以傳送無限參數 keyword args
    print(kwargs) # 所有參數被kwargs蒐集，根據參數"鍵=值 "成為一個字典(dict)


user_info6 (age=99,keyword=332,apple="睡覺") # 注意:是關鍵字
user_info6 (pp=11,org=22,eew=33)



