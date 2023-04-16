

# 黑馬atm


def atm() :
    money = 5000000
    name = input("請輸入您的姓名:")
    flag = True
    while flag:
        a=input(f'\n{name}您好!\n\n查詢餘額    [輸入1]\n存款        [輸入2]\n取款        [輸入3]\n退出        [輸入4]\n\n請輸入您要選擇的服務:')
        if a == "1":
            print("\n--------查詢餘額--------")
            print(f"您的餘額為 : {money}")
            print("------------------------")
        elif a == "2":
            print("----------存款----------")
            b=int(input("請輸入要存放的金額 : "))
            money += b
            print(f"您的餘額為 : {money}")
            print("------------------------")        
        elif a == "3":
            print("----------取款----------")
            b=int(input("請輸入要取出的金額 : "))
            if (money-b) < 0:
                print("餘額不足")
                print(f"您的餘額為 : {money}") 
                print("------------------------")  
            else :
                money -= b
                print(f"您的餘額為 : {money}")
                print("------------------------")
        elif a == "4":
            print("\n感謝您的使用，歡迎再次光臨")
            print("--------退出服務--------")
            flag = False
        else :
            print("\n操作錯誤，請重新使用本系統")
            print("--------操作錯誤--------")
            flag = False

atm()


        