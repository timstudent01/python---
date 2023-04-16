


# end = '' 可以不換行
# \t 可以讓單字多行輸出時能夠對齊


cols = 1
while cols <= 9 :
    rows = 1 
    while rows <= cols:
        print(f'{rows}*{cols}={cols*rows}\t', end='')
        rows += 1
    cols += 1
    print()


i = 1
while i <= 9 :
    j = 1
    while j <= i :
        print(f'{i} * {j} = {i*j}\t', end='')
        j += 1
    i += 1
    print()



a = 1
while a <= 9 :
    b = 1
    while b <= a :
        print(f'{a}*{b}={a*b}\t' , end = '')
        b += 1
    a += 1
    print() 