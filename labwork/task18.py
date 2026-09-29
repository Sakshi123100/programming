l=[33,9,0]

for i in range(0,len(l)):
    for j in range(1+i,len(l)):
        l[j],l[i]=l[i],l[j]

print(l)