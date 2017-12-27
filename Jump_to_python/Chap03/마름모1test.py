a=0
while True:
    a = int(input("홀수를 입력하세요(0입력시 종료): "))
    if a==0:break
    if a%2 == 0:
        print("짝수를 입력했습니다. 다시 입력하세요")
        continue
    for b in range(1,a+1):
        if b%2==1:
         print(b*"*")