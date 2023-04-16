print("Hello World!!")
print("你好世界")
print('零基礎學IT就來黑馬程序員')
print("")

# 字面量: 在代碼中被寫下來的固定的值


                # python常用的六種類型

# 1. 數字 Number       int float complex boolean
# 2. 字符串 String     任意數量的字符 需要用" "包圍起來
# 3. 列表 List         
# 4. 元組 Tuple
# 5. 集合 Set
# 6. 字典 Dictionary

print("黑馬程序員")

# 單行註釋 # 多行註釋"""" """
money=500
# print 中數據 使用逗號隔開
print("錢包還有:",money)
money -= 10

print("錢包還有:",money)

print("我超帥"+"我超強",money)

# 字符串無法直接和數字類型變數拼接
# 若是變數是字串則可以透過+號拼接
money_string = str(money)
print("我超帥"+"我超強"+money_string)

# 字符串格式化 (佔位型拼接)
# % 表示: 我要佔位
# s 表示: 將變量變成字符串放入佔位的地方
name = "黑馬程序員"
message = "學IT就來 %s" % name

# 將name 放入%的地方
print(message)

# 多佔位
class_num = 57
avg_salary = 16781 
message = "Python大數據學科，北京%s期，畢業平均工資: %s" % (class_num, avg_salary)
print(message)


# 數據類型佔位，支持很多種，常用為下面三個:

# %s 將內容轉換為字符串，放入佔位位置
# %d 將內容轉換為整數，放入佔位位置
# %f 將內容轉換為浮點數，放入佔位位置
name = 78889
name_123 = type(name)
print (type(name_123))
print (name_123)

name2 = "傳智播客"
setup_year = 2006
stock_price = 19.99

message = "%s，成立於:%d，我今天的股價是 %f" % (name2 , setup_year , stock_price) 
print(message)

# 數字精度控制

# m 控制寬度，要求是數字(很少使用)，設置的寬度小於數字本身則無效
# .n 控制小數點精度，要求是數字，會進行小數四捨五入
# m .n 都可以省略


# 範例: %5d :表示將整束的寬度控制在5位，如數字11，被設置為5d，就會變成[空格][空格][空格] 11，用3個空格補足寬度。
# 範例: %5.2f :表示將寬度控制為5，將小數精度設置為2
# 小數點和小數也會納入寬度計算，例如將11.345設置為%7.2f，結果是[空格][空格]11.35。2個空格補足寬度，小數部分被限制為2位後，會四捨五入為.35。
# %.2f :表示不限制寬度，只設置小數點精度為2，如設置11.345設置%2f後，顯示11.35。

message = "%s，成立於:%d，我今天的股價是 %.2f" % (name2 , setup_year , stock_price) 
print(message)


# 快速格式化寫法
# 語法: f"內容{變數}" 的格式實現快速格式化
# f : format 
message = f"{name2}，成立於:{setup_year}年，我今天的股價是:{stock_price} " 
print(message)


name = "傳智播客"
stock_price = 19.99
stock_code = '003032' 
stock_price_daily_factor = 1.2 # 股票增長係數
growth_days = 7

print(f"公司:{name}，股票代碼:{stock_code}，當前股價:{stock_price}")
print("每日增長係數為:%.1f，經過%d天的增長後，股價達到了:%.2f" %(stock_price_daily_factor, growth_days , stock_price*stock_price_daily_factor**growth_days))

