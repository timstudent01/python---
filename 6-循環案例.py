
import random
num = random.randint(1,100)

i = 0
time = 0


while i <= 100 :
    answer = int(input("猜猜樂囉，來猜數字1~100 :"))
    if  answer == num :
        time +=1 
        print("恭喜您猜對了，答案是:%d" % num)
        print("您一共猜了%d次" % time)
        time = 0
        i = 101
    else :
        if answer < num :
            time += 1
            print("猜錯囉，數字要再大一點，您已猜了%d次" % time)
            i = 0

        else :
            time +=1 
            print("猜錯囉，數字要再小一點，您已猜了%d次" % time)
            i = 0
               


import random
num = random.randint(1,100)
flag = True
time = 0


while flag:
    answer = int(input("猜猜樂囉，來猜數字1~100 :"))
    time += 1
    if  answer == num :
        print("恭喜您猜對了，答案是:%d" % num)
        time = 0
        flag = False
    else :
        if answer < num :
            print("猜錯囉，數字要再大一點，您已猜了%d次" % time)
        else :
            print("猜錯囉，數字要再小一點，您已猜了%d次" % time)

print("您一共猜了%d次" % time)
