


# 定義 金錢 名字
money = 5000000
name = input("請輸入您的姓名 : ")

# 定義存款
def saving(num):
    global money
    money += num
    print(f"{name}，您好，您存款 {num} 元成功 ")
    print(f"{name}，您好，您的餘額為 : {money}")
    print("\n----------------------------------")

# 定義取款
def getting(num):
    global money
    money-=num
    print(f"{name}，您好，您取出 {num} 元成功 ")
    print(f"{name}，您好，您的餘額為 : {money}")
    print("----------------------------------")

# 定義查詢餘額
def leaving():
    global money
    print("\n-------------查詢餘額-------------")
    print(f"{name}，您好，您的餘額為 : {money}")
    print("----------------------------------")

# 定義主菜單
def main():
    print(f"{name}，您好，歡迎來到黑馬ATM，請選擇操作。\n")
    print("----------------------------------")
    print("查詢餘額\t[輸入1]")
    print("存款\t\t[輸入2]")
    print("取款\t\t[輸入3]")
    print("退出服務\t[輸入4]")
    print("----------------------------------")
    return input("請輸入您要的服務選項 : ")

# 設置無限循環
flag = True
while flag:
    key_board_input = main()
    if key_board_input == "1":
        leaving()
        continue
    elif key_board_input == "2":
        print("\n---------------存款---------------")
        num = int(input(f"{name}，您好，請輸入您要存放的金額 : "))
        saving(num)
        continue
    elif key_board_input == "3":
        print("\n---------------取款---------------")
        num = int(input(f"{name}，您好，請輸入您要取出的金額 : "))
        if money < num :
            print("餘額不足，請重新操作一次")
            print("----------------------------------")
        else :
            getting(num)
            continue
    elif key_board_input == "4":
        print("感謝您的使用，歡迎再次光臨")
        print("\n-------------退出服務-------------")
        flag = False
    else :
        print("操作錯誤，請重新使用本系統")
        continue