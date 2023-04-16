
# 1. 打開文件 a模式
f = open("C:/Users/timst/OneDrive/圖片/桌面/PYTHON黑馬/測試6.txt","a",encoding="UTF-8")

# 2. 文件寫入 
f.write("hello world\n") # 內容寫入內存中

# 3. 內容刷新
f.flush() # 將內存中積攢的內容，寫入到硬碟文件中

# 4. close() 如果不調用flush() 直接close 也內建flush()功能
f.close()

# 注意: 文件存在會消除原有內容並寫入，若是沒有文件則會創建。