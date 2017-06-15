list=[]
for i in range(2000, 3000):
    if (i%5==0) :
        list.append(str(i))

print (','.join(list))