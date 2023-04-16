
# def 關鍵字，可以定義"帶有名稱"的函數
# lambda 關鍵字，可以定義"匿名函數"(無名稱)

# 有名稱的函數，可以基於名稱重複使用。
# 無名稱的匿名函數，只可臨時使用一次。

# 匿名函數定義語法:
# lambda 傳入參數: 函數體(一行代碼)
# ．lambda 是關鍵字，表示定義匿名函數
# ．傳入參數表示匿名函數的形式參數，如: x,y 表示接收2個形式參數
# ．函數體 就是函數的執行邏輯，要注意: 只能寫一行，無法寫多行代碼

def test_func(compute):
    result = compute(1,2)
    print(result)

test_func(lambda x , y : x + y) # 結果為 3

def testA(S):
    answer = S(1,3,5,67,77)
    print(answer)
    
def testB(d,e,f,g,h):
    return d+e+f+g+h

testA(testB)

testA(lambda d,e,f,g,h : d*e*f*g*h)


def testG(*G):
    GG=1
    for gg in G :
        print(gg)
        GG*=gg
    return GG

print(testG(12,10,11,15))

odd_or_even = lambda x : not x%2   # 請將-----變更為匿名函數
print(odd_or_even())

