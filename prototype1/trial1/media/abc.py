textfile = open('results.txt', 'wt')
l1 = open("weakphrase.txt", "r").read().split('\n')
l2 = open("Story creation-Rockwell.txt", "r").read().split()
file3 = open("results.txt", "a")
#print(l1)

#print(l2)
for j in range(1,len(l2)):
    if l2[j]=='as':
        if (l2[j+1]=='required') | (l2[j+1]=='appropriate'):
            l2.append(l2[j]+' '+l2[j+1])
    elif l2[j]=='be':
        if (l2[j+1]=='capable') & (l2[j+2]=='of'):
            l2.append(l2[j]+' '+l2[j+1]+' '+l2[j+2])
        elif (l2[j+1]=='able') & (l2[j+2]=='to'):
            l2.append(l2[j]+' '+l2[j+1]+' '+l2[j+2])
    elif l2[j]=='capability':
        if (l2[j+1]=='to') | (l2[j+1]=='of'):
            l2.append(l2[j]+' '+l2[j+1])

l3=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
unique_ = set(l3) 
for words in unique_ : 
        print(words , ' :', l3.count(words))
        file3.write(words +' ' + str(l3.count(words))+'\n')