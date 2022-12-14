# 尋找兩數間的質數
a = int(input("First Number?"))
b = int(input("Second Number?"))
Line5 = 0
Line7 = 0
Line8 = 0
Line9 = 0
Line10  = 0
if a>b:
    a,b = b,a
    Line5+=1
NotPrimeNum = [1]
for i in range(a+1,b):
    Line7+=1
    for j in range(1,i):
        Line8+=1
        if i %j == 0 and j!=1:
            Line9+=1
            NotPrimeNum.append(i)
            Line10+=1
Numbers = set({i for i in range(a+1,b)})
PrimeNum = Numbers - set(NotPrimeNum)
print(PrimeNum)
