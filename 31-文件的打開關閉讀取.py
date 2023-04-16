

# 打開文件的函數 open(name,mode,encoding)

# name : is a string of target file that you would like to open.
# mode : setting a mode to open file.
# encoding : 編碼格式 (推薦使用UTF-8)

# f = open ("C:/Users/timst/OneDrive/圖片/桌面/PYTHON黑馬/測試1.txt","r",encoding="UTF-8")

# The order of encoding is not the third,so you can't use position parameter,
# you should use "key word" to assign.
# 上面意思是編碼格式不是順序第三位，所以不能用位置參數，只能用關鍵字參數指定
# open 函數 默認第三位是buffering

# Noticing: 此時的 f 是"open"函數的文件對象，對象是Python中醫種特殊的數據類型，
#           擁有屬性和方法，可以使用對象、屬性或對象方法進行訪問。

#      <<mode 常用的三種基礎訪問模式>>

# 1. r :"只讀"方式打開文件，這是默認模式。

# 2. w :打開文件只用於"寫入"。如果該文件已存在則打開文件，並從頭開始編輯，
#       原有內容會被"刪除'。如果該文件不存在，創建新文件。  

# 3. a :打開一個文件用於"追加"。如果該文件已存在，新的內容將會寫入到已有內容之後。
#       如果該文件不存在，創建新文件進行寫入。


# (1.) 打開文件



f = open ("C:/Users/timst/OneDrive/圖片/桌面/PYTHON黑馬/測試1.txt","r",encoding="UTF-8")
print(type(f))

# (2.) 讀取文件 read() 讀取的是字符串
# print(f.read())   讀取全部文件資料
print(f.read(20)) # 只讀取20個字符
print(f.read(20)) # 第二次讀取會從第一次讀取斷點開始讀取
# read = f.read()
# print(type(read)) # 文件 type的類別檢查若使用read函數 也會繼續讀取文件內容

# (3.) 讀取文件 readlines() 讀取出的是list形式
#      會續接read()的斷點

# lines = f.readlines()
# print(type(lines))

print(f.readlines(40))

# (4.) 讀取文件單行 readline() 一次讀取一行
print(f.readline())
print(f.readline())
print(f.readline())


n=1
for x in f:
    print(f"第{n}行數據為: {f.readline()}")
    n+=1

# 解除文件的運行 .close()

f.close()
print('已結束文件的開啟')

# with open 執行完成後就會關閉文件，避免遺忘.close()
# 語法: with open(路徑,讀取方式,編碼方式) as e:
with open("C:/Users/timst/OneDrive/圖片/桌面/PYTHON黑馬/測試2.txt","r",encoding="UTF-8") as e:
    h = 1
    for line in e:
        print(f"第{h}行數據為 : {e.readline()}")
        h+=1

keti = open("C:/Users/timst/OneDrive/圖片/桌面/PYTHON黑馬/測試3.txt","r",encoding="UTF-8")

keti_read = keti.read()
print(keti_read)


k_c = keti_read.count("itheima")
print(k_c)

keti.close

# 第二種方法 
keti = open("C:/Users/timst/OneDrive/圖片/桌面/PYTHON黑馬/測試3.txt","r",encoding="UTF-8")
count=0
for line in keti:
    line = line.strip() # 去除前後空格
    x = line.split(" ") # 以空格分割
    for word in x:
        if word == "itheima":
            count += 1
    print(line)
    print(x)

print(count)
    