def func_b():
    print("--2--")

def func_c():
    print("--1--")

    func_b()

    print("--3--")

func_c()


# 利用global聲明，可以變成全局變量

num = 200

def test_a():
    num =300
    print(f"test_a:{num}")

def test_b():
    global num
    num = 500
    print(f"test_b:{num}")

test_a()

print(num)


test_b()

print(num)