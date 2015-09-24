vvod= input() .split( )
spisok=[int(x) for x in vvod]
even= list()
odd= list()
for i in range(0, len(spisok)):
    if i%2!=0:
        even += [spisok[i]]
        list.sort(even)
        list.reverse(even)
    else:
        odd += [spisok[i]]
        list.sort(odd)
#print (even)
#print (odd)
n=0
k=0
result=list()
for a in range(0, len(spisok)):
    if a%2!=0:
        result += [even[n]] 
        n+=1
    else:
        result += [odd[k]] 
        k+=1
print (" ".join(str(s) for s in result))
