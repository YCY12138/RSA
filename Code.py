def text_to_code(text):#将字符转化为gb2312编码
    dat=text.encode("gb2312")
    return dat
    

def text_to_num(character):#将单个字符的gb2312编码转换为可以进行计算的int型数
    if(len(character)==2):
        high=int(character[0])
        low=int(character[1])
        result=high*1000+low

    if(len(character)==1):
        result=int(character[0])
    return result
