# import time # time.py 搬運整個模組

# time.sleep(5)

from time import sleep # 指搬運time裡面的sleep函數

try:
    print("耶")
    sleep(2) # 只導入sleep，不可以用time.sleep來召喚
    print(2)
except Exception as e:
    print(e)


# 使用*來全部導入time模組所有功能 from time import *
# 此時的語法中直接使用 sleep就可以，不可以用time.sleep來導入
# 不過不推薦使用此語法

from d_自定義模組 import test_A

test_A()

from mod123 import test_B

test_B()

print({1,2,3,4,3,2})