# 嵌套的關鍵點，在於: 空格縮進
# 通過空格縮進，來決定語句之間的: 層次關係


# 我的
import random
num = random.randint(1,10)

answer = int(input("有三次機會，1~10請輸入猜測的數字:"))
if answer == num :
    print("恭喜您答對了")
elif answer > num :
    print("猜錯囉，數字要小一點")
    answer = int(input("請輸入第二次猜測的數字:"))
    if answer == num :
        print("恭喜您第二次答對了")
    elif answer > num :
        print("猜錯囉，數字要再小一點")
        answer = int(input("請輸入第三次猜測的數字:"))
        if answer == num :
            print("恭喜您，終於猜對了")
        else :
            print("三次都沒猜中，真可惜，答案是%s，下次加油囉" % num)
    elif answer < num :
        print("猜錯囉，數字要再大一點")
        answer = int(input("請輸入第三次猜測的數字:"))
        if answer == num :
            print("恭喜您，終於猜對了")
        else :
            print("三次都沒猜中，真可惜，答案是%s，下次加油囉" % num)  
elif answer < num :
    print("猜錯囉，數字要大一點")
    aanswer = int(input("請輸入第二次猜測的數字:"))
    if answer == num :
        print("恭喜您第二次答對了")
    elif answer > num :
        print("猜錯囉，數字要再小一點")
        answer = int(input("請輸入第三次猜測的數字:"))
        if answer == num :
            print("恭喜您，終於猜對了")
        else :
            print("三次都沒猜中，真可惜，答案是%s，下次加油囉" % num)
    elif answer < num :
        print("猜錯囉，數字要再大一點")
        answer = int(input("請輸入第三次猜測的數字:"))
        if answer == num :
            print("恭喜您，終於猜對了")
        else :
            print("三次都沒猜中，真可惜，答案是%s，下次加油囉" % num)

# 黑馬的
answer = int(input("有三次機會，1~10請輸入猜測的數字:"))
if answer == num :
    print("恭喜您答對了")
else :
    if answer > num :
        print("猜錯囉，數字要小一點")
    else :
        print("猜錯囉，數字要再大一點") 
    
    answer = int(input("請輸入第二次猜測的數字:"))
    
    if answer == num :
        print("恭喜您第二次答對了")
    else :
        if answer > num :
            print("猜錯囉，數字要小一點")
        else :
            print("猜錯囉，數字要再大一點")

        answer = int(input("請輸入第三次猜測的數字:"))
        if answer == num :
            print("恭喜您第三次答對了")
        else :
            print("三次都沒猜中，真可惜，答案是%s，下次加油囉" % num)