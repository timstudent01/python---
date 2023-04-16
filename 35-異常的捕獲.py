
# 捕捉異常

# 語法:
# try:
#   f = open('linux.txt','r') 可能發生錯誤的代碼
# expect:
#   f = open('linux.txt','w') 如果出現異常執行的代碼

# 捕獲指定異常

# 語法: 
# try:
#   print(name)
# except NameError as e:
#   print("name變數名稱未定義錯誤")

try:
  print(name)
except NameError as e: # e是異常的報告
  print("出現了未定義錯誤")
  print(e)

# 捕獲多個異常
# 語法:
try:
  print(1/0)
except (NameError,ZeroDivisionError):
  print("ZeroDivisionError 錯誤")


# 捕獲所有異常
# 語法:
try:
    print(gg)
except Exception as f:
    print("出現異常了")
    print(f)
    
# else:
# 若加在try: except: 後面，沒異常的時候會執行

# finally:
# 無論如何會執行的語句

try:
    print(mmm)
    print("讓else執行的神奇文字，才怪，有異常就不會執行了")
except Exception as ggg:
    print(ggg)
    print("gg")
else:
    print("沒異常")
finally:
    print("我最後一定會執行，幹好累") 


# 異常的傳遞性質
# 當函數調用時，如果函數嵌套中發生異常，可以用函數直接捕獲異常
# 異常的冒泡

