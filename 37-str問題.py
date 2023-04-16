m = int(input("Input factorial: "))
r = 1
n = 1

while n <= m :
    r *= n
    n += 1

print(str(m)+"! =",r)


for i in range(1,10):

    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}\t", end=" ")
    print("")
   
