import Check_num
import random


def prime_num():#返回一个随机生成的大素数
    k=random.randint(23413534,645747879)
    while(not Check_num.isPrimeByMR(k)):
        k=k+1

    return k
    
    
def key():#返回存储着公钥和私钥的列表
    
    p=prime_num()
    q=prime_num()
    n=p*q
    Eulern=(p-1)*(q-1)
    
    e=random.randint(1,Eulern)
    while(gcd(e,Eulern)!=1):
        e=e+1

    d=extend_Euclid(Eulern,e)
    if(d<0):
        d=d+Eulern
    print("公钥为:(%d,%d)" %(n,e))
    print("私钥为:(%d)"%(d))
    keys=[n,e,d]

    return keys
    


def gcd(a,b):#求最大公因数
    if b == 0 : return a
    return gcd(b,a % b)

def extend_Euclid(a,b):#扩展欧几里德算法 返回逆元
    if(b==0):
        d=a
        x=1
        y=0

    x2=1
    x1=0
    y2=0
    y1=1
    while(b>0):
        q=a//b
        r=a-q*b
        x=x2-q*x1
        y=y2-q*y1
        a=b
        b=r
        x2=x1
        x1=x
        y2=y1
        y1=y

    d=a
    x=x2
    y=y2
        
    return y


