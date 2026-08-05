"""
for i in range(3,31,3):
    print(i)

for i in range(3):
    for j in range(2):
        print(i,j)


i=1
while i<=5:
    print(i)
    i+=1


for i in range(1,10):
    if i==5:
        break
    print(i)

for i in range(1,10):
    if i==3:
        continue
    print(i)

for i in range(1,10):
    if i==3:
        pass
    print(i)


num=5
fact=1
while num>0:
    fact=fact*num
    num= num - 1
print(fact)

"""
minutes = 145
hours = minutes // 60
remaining_minutes = minutes % 60
print("Total time is:",hours,"hours and",remaining_minutes,"minutes")