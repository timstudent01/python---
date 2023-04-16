

# 2<<2 2*(2**2)=8
 
# 3<<4 3*(2**4)=48    


# <<n 表示 *2的n次方 >>n 表示 /2的n次方


str1 = "hello python"

print(str[2:-1:3]) # l t

# python 沒有陣列型態

# 字串的.split　也有反轉版 .rsplit 
# rsplit(",",maxsplit=1)[:-1]
str2 = "hello,python,我超帥,我一級棒"
str2.rsplit(",",maxsplit=1)[:] # maxsplit = n 最多用幾個,分隔 

print(11,12) # 輸出: 11 12 預設中間有空格 若要換則 +,sep="n" n為任意字元

print(11,12,sep="|")

print(11,12,end=" ")
print(13,14,end=" ") # emd 預設為\n 換行 

# eval(input()) 可以將input內容變成int 

a = eval(input("請輸入數字1: "))
b = eval(input("請輸入數字1: "))
print(a+b)

# 跑程式 在命令提示字元語法 cd 位置 (不知道是否適用)

a = eval(input("請輸入數字1: "))
b = eval(input("請輸入數字1: "))
print(a+b)

# 三元運算

0 if 8 else 9 # 如果 8 為真 則呈現0 若為假 則呈現 9

0 if False else 10 # False 所以是 10
a = "我好帥"
h = eval(input("Enter hour(0-23): "))
h = h%24 if h >=24 else h 
print('Current time = {}:00{}'.format(h,a))

# "{}" .format()     {}是預留空位 後面()填入變數

m = int(input("Input factorial: "))
r = n = 1

while n <= m :
    r *= n
    n += 1

print(str(m)+"! =",r)

# print(r)
# print(n)

# if m = 5 
# r=r*n = 1*1 r=1
# n=n+1 = 1+1 n=2

# r=r*n 1*2 r=2
# n=n+1 = 2+1 n=3

# 列表由小到大排序 sorted
y=[1,7,8,9,225,4]
x=sorted(y)
z=sorted(y,reverse=True)
print(x)
print(z)


# not語句 目前理解為 ddd-fff == 0  相等於 not ddd-fff 
# 而 ddd%fff !=0 相當於 ddd%fff包含在第一個not語句之後，且中間無not
# 單元運算法 速度 優於二元運算法
ddd= int(input("數字1"))
fff= int(input("數字2"))

if not ddd-fff and not ddd%fff:
    print("0")
else:
    print("100")



# 函數

# 字典遍歷
data_dict = {"BDSE": 22, "AIEN": 20, "AIOT": 32, "SESE": 32} 


data_dict["MFEE"]=25

print(data_dict)

data_dict_keys=data_dict.keys()

for ghg in data_dict_keys:
    print(ghg,data_dict[ghg],end=" ")
print("dtype:int64",end=" ")

# 匿名函數