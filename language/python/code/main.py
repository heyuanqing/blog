print("hello world")
a = 1
print("del qian " ,a)
# del a
# print("del hou " ,a)

Money = 2000

def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1
print (Money)
AddMoney()
print (Money)
