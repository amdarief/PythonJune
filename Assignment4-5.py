origlist = [5,6,4,7,2,9,10,5,6,7,101,11,51,9]
uniqlist = []
for i in origlist:
   if i not in uniqlist:
       uniqlist.append(i)
print (uniqlist)