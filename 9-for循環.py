# for循環語法:

#   for 臨時變量 in 待處理數據集(序列) :
#       循環滿足條件執行的代碼

value = [3,4,5]

for x in value:
    print(x)

# 與while循環不同，for 循環 無法定義循環條件。
# 理論上 Python 的 for 循環 無法購建無限循環。
count = 0
a = "itheima is a brand of itcast"
for x in a:
    if x == "a":
        count += 1
print(f'{a} 中共含有 : {count}個字母a')

