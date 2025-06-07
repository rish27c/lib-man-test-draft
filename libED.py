from time import sleep as wait

d_en={
    'a':'akfht', 'b':'gjtnd', 'c':'khjtn', 'd':'ekfng', 'e':'kgntr', 'f':'lgktr', 'g':'gkrna', 'h':'gjter', 'i':'jghre', 'j':'kfjtr', 'k':'pqmkv', 'l':'tkbpz', 'm':'zmbrg', 'n':'tneam', 'o':'mcnas', 'p':'mzsan', 'q':'tmali', 'r':'maort', 's':'tyrpq', 't':'amlyh', 'u':'tmadf', 'v':'apotr', 'w':'malyh', 'x':'lgtre', 'y':'nhgky', 'z':'rghmf',
    '1':'ktpng', '2':'ngler', '3':'bhrzq', '4':'qaser', '5':'ynapm', '6':'pahtz', '7':'gnegh', '8':'atndi', '9':'grpae', '0':'toage', ' ':'olloo', '.':'llool', '@':'terte', '$':'pwabg', '&':'laqer', '(':'ferte', ')':'etref', '*':'tared', '!':'lform', '#':'kjeqw', '~':'retnj'
}

def en(inp:str, manual:bool=False):
    ilist=[]
    if manual==True:
        symbol=False
        for i in inp:
            if i not in list(d_en.keys()) and i.lower() not in list(d_en.keys()):
                symbol=True
        if symbol==True:
            symbols=str(ilist)[1:-1]
            print('Invalid input, libED:bad input<-Break;\n\t\tUse of symbols detected.')
            raise ValueError(f'libED::"Use of symbol(s):{symbols}"')
        else:
            enp=''
            for ei in inp:
                if ei<='Z' and ei>='A':
                    ei=ei.lower()
                    enp+=d_en[ei].upper()
                else:
                    enp+=d_en[ei]
            return enp
    else:
        raise ModuleNotFoundError('libED::"Using raw libEd function without proper args"')


def ed(inp:str, manual:bool=False):
    if manual==True:
        if inp==None or inp=='':
            raise ValueError('libED::"Empty String->NoneType"')
        elif len(inp)>2500:
            print('libED->Error:Too large string to process.')
            raise IndexError('libED::"The length of characters surpasses the input limit"')
        elif len(inp)%5!=0:
            raise IndexError('libED::"The string is incomplete or broken"')
        else:
            enp=''
            for i in range(0, len(inp), 5):
                ei=inp[i:i+5]
                if ei[0]<='Z' and ei[0]>='A':
                    ei=ei.lower()
                    for ai in list(d_en.keys()):
                        if d_en[ai]==ei:
                            enp+=ai.upper()
                else:
                    for ai in list(d_en.keys()):
                        if d_en[ai]==ei:
                            enp+=ai
            return enp
    else:
        raise ModuleNotFoundError('libED::"Using raw libEd function without proper args"')

def libcrypt(scanf:str, process:str, add:dict={}, security_level:int=1):
    d_en.update(add)
    if process=='encrypt':
        ec=scanf
        for loop in range(security_level):
            ec=en(ec, True)
    elif process=='decrypt':
        ec=scanf
        for loop in range(security_level):
            ec=ed(ec, True)
    else:
        print('libED->Error: Invalid process.')
        raise SyntaxError('libED::"Invalid process for libcrypt function"')
    return ec

def compresser(inp:str):
    if inp[-1]!='-':
        inp+='-'
    else:
        inp+='+'
    a=inp[0]
    c=0
    comlist=''
    i=0
    while i<len(inp):
        if inp[i]==a:
            c+=1
        else:
            comlist+=f"{c}{a}"
            c=0
            a=inp[i]
            i-=1
        i+=1
    return comlist

def decompresser(inp:str):
    i=0
    num=''
    char=''
    while i<len(inp):
        if inp[i].isdigit():
            num+=inp[i]
        else:
            char+=inp[i]*int(num)
            num=''
        i+=1
    return char

if __name__=='__main__':
    print('DO NOT TOUCH THE FILE!')
    wait(5)