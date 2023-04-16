flower = 0
day = 1
while day <= 100 :
    print("今天是第%d天，準備表白......" % day)
    flower = 1 
    while flower <= 10 :
        print("送小美第%d朵花" % flower)
        flower += 1
    print("小美我喜歡你")
    day += 1

print("告白到第%d天，告白成功" % (day-1)) 