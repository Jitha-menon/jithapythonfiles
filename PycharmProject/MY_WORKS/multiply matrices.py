m1=[[5,6],[2,3]]
m2=[[2,3],[5,6]]
r=[[0,0],[0,0]]
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            r[i][j]+=m1[i][k]*m2[k][j]
print(r)



