
# 創立正常的py文件，在裡面寫函數，就可以使用import導入

# 模組被導入的時候。若是執行文件，則模組的函數會直接運行

# 所以需要透過 if __name__ == __main__: 來避免

# 如果模組中有 __all__ ，則*不一定能調用所有變數。
# 

__all__ = ["test_A"]

def test_A():
    print("testA2")

def test_B():
    print("testB2")





