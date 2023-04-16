# 假如使用者帳號是Jack，密碼是1234 列印出 Hello Jack

if input("請輸入帳號: ") == "Jack":
    if input("請輸入密碼: ") == "1234":
        print("Hello Jack")
else:
    print("輸入錯誤")


# 如果每個月底(每個月最後一日)固定存款1萬元台幣，銀行的年利率是5%，
# 每月採用複利計算。請問如果要存到100萬元，需經過幾個月存款呢? 建議使用while loop來解這個問題。
money = 0
moon = 0
while money < 1000000 :
    money*=1.05
    money+=10000
    moon+=1
    print(moon)
    print(money)

print(moon)
print(money)


# 閏年的規則為： 「公元年分除以4可整除但公元年分除以100不可整除」 
# 或 「公元年分除以400可整除」 公元是以1年開始計算的，請利用迴圈與Tuple，
# 把截至2020年的所有閏年放入一個Tuple中，並用print(Tuple)輸出結果。

tuple_year=[]
# for loop start

for year in range (1,2021):
    if year % 100 != 0:
        if year % 4 == 0:
            yearadd = [year]
            tuple_year.append(year)
        else: 
            if year % 400 == 0:
                tuple_year.append(year)

print(tuple(tuple_year))

# 現有兩個集合： s1 = {1,2,3,4,5} s2 = {4,5,6,7,8} 請求出這兩個集合的聯集，並用print()函數顯示出來
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1&s2)