
def test_func():
    result = compute(1,2)
    result2 = compute2(12,23)
    result3 = compute3(12,23)
    result4 = compute4(11,22)
    print(result)
    print(result2)
    print(result3)
    print(result4)

def compute(x,y):
    return x + y

def compute2(x,y):
    return x * y

def compute3(x,y):
    return x / y

def compute4(x,y):
    return x - y 

print(test_func())
c = 1
test_func()
# 函數compute 作為參數，傳入test_func函數中使用。
# test_func 需要一個"函數"作為"參數"傳入，這個函數需要接收"兩個數字"進行計算，計算邏輯由這個被傳入函數決定。
# compute函數接收兩個數字對其進行計算，compute函數作為參數，傳遞給了test_func函數使用
# 最終，在test_func函數內部，由傳入的compute函數，完成了對數字的計算操作

def test_func2(compute5):
    result = compute5(1,2)
    print(result)

def compute5(x,y):
    return x * y

test_func2(compute5)