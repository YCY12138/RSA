def Function(a,index,m):#重复平方乘算法
    index_2_a=bin(index)
    index_2=[]

    for i in range(0,len(index_2_a)-2):
        index_2.append([])
    
    for k in range(0,len(index_2)):
        index_2[k]=(int)(index_2_a[len(index_2_a)-k-1])
        
    b=1

    if(index==0):
        return b
    A=a
    if(index_2[0]==1):
        b=a

    for i in range(1,len(index_2)):
        A=(A**2)%m
        if(index_2[i]==1):
            b=(A*b)%m


    return b


