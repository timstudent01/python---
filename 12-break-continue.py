# continue 循環臨時中斷

import random
j = 10000

for i in range(1,21):
    num = random.randint(1,10)
    if num < 5:
        print(f"員工{i}，績效分{num}，低於 5 ，不發工資，下一位。")
    else :
        j-=1000
        print(f'員工{i}，高於需求績效分，發放工資 : 1000元，公司帳戶餘額還剩下 : {j}元')
        if j <= 0 :
            break
print("工資發完了，下個月領取吧")

