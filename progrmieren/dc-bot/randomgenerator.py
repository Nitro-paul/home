import random
def generate(argument:str):
    if argument[0:3]=="num":
        lengh=str(argument[4:len(argument)])
        if lengh=="":
            lengh=1
        random=0
        source=list[0,1,2,3,4,5,6,7,8,9]
        for i in lengh:
            random+=random.choice(source)
        out1=random
    else:
        out1="unknown arguments used"
    return str(out1)