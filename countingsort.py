from stringtolist import strtolist

minvalue = min(intlist)
maxvalue = max(intlist)

succession = {}

i = minvalue
while i <= maxvalue:
    succession[i] = 0
    i = i + 1

for i in intlist:
    if i in succession:
        succession[i] = succession[i] + 1
    
c = 1
while c<= len(succession) - 1:
    succession[c] = succession [c] + succession[c-1]
    c = c+1


    


c = len(succession)-1
while c >= 0:
    if c == 0:
        succession[c] = 0
        break
    succession[c] = succession[c-1]
    
    c = c-1
    


sorted_list = []
for i in intlist:
    sorted_list.append(0)


temp = 0
for i in intlist:
    
    temp = succession[i]
    sorted_list[temp] = i
    succession[i] = succession[i] + 1
    

print(sorted_list)
