
# 備份文件 (去掉測試 填入正式)

f = open("C:/Users/timst/OneDrive/圖片/桌面/PYTHON黑馬/bill.txt","r",encoding="UTF-8")
f2 = open("C:/Users/timst/OneDrive/圖片/桌面/PYTHON黑馬/bill2.txt","w",encoding="UTF-8")
f3 = open("C:/Users/timst/OneDrive/圖片/桌面/PYTHON黑馬/bill3.txt","w",encoding="UTF-8")
f4 = open("C:/Users/timst/OneDrive/圖片/桌面/PYTHON黑馬/bill4.txt","w",encoding="UTF-8")


for line in f:
    line = line.strip()
    line2 = line.split(",")
    if line2[4] == "測試":
        continue
    f2.write(line)
    f2.write("\n")
    f3.write(line)
    f3.write("\n")
    f4.write(line)
    f4.write("\n")


     # write 不能寫列表



f2.close()
f3.close()
f4.close()