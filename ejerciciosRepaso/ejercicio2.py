from functools import reduce
listNum=[7,4,8,6]
x = reduce(lambda x,y:f"{x}{y}",listNum)
print(x)
