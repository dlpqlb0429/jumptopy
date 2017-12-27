a=3
b=4

def sum(a,b):
    if a==0 and b==0:
        print("양수만 입력하세요.")
        return 0
    return a+b

c=sum(a,b)
print(c)
a=0
b=0
c=sum(a,b)
print(c)


