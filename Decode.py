import Code
import RSA_keys
import Repeat_

def new(size):
    newlist=[]
    for i in range(0,size):
        newlist.append([])

    return newlist

print("请输入要进行加密的文本")
text=input()


gbtext=new(len(text))

for i in range(0,len(text)):#将每个汉字对应的6位码存储到一个数组里
    gbtext[i]=Code.text_to_num(Code.text_to_code(text[i]))
    


keys=RSA_keys.key()#得到用来加密的公钥和私钥
text_Encrypted=new(len(text))#创建一个同样大小的数组来存储加密后的信息

for i in range(0,len(text)):#得到了加密过后的信息
    text_Encrypted[i]=Repeat_.Function(gbtext[i],keys[1],keys[0])

text_Decrypted=new(len(text))

for i in range(0,len(text)):#算出解密后的数
    text_Decrypted[i]=Repeat_.Function(text_Encrypted[i],keys[2],keys[0])

for i in range(0,len(text)):#打印出加密后存储的数以及解密后存储的数
    print(text_Encrypted[i])
    print(text_Decrypted[i])

for i in range(0,len(text)):#打印出根据解密后的数得到的text信息
    if(text_Decrypted[i]//160160==1): 
        arr=bytearray([text_Decrypted[i]//1000,text_Decrypted[i]%1000])
        print(arr.decode("gb2312"))

    if(text_Decrypted[i]//160160==0):
        arr=bytearray([text_Decrypted[i]])
        print(arr.decode("gb2312"))


    


