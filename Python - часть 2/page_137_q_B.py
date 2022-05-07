def Byte1(n):
    return(n<256)
i = int(input("enter the number: "))
print("number",i,"byte:",Byte1(i))