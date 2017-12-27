#가로 최대 길이를 입력받아 마름모 출력하는 프로그램 작성
#출력 마름모 프로그럼 Ver[]
#   홀수를 입력하세요(0종료) :
#    짝수 입력시 > 짝수를 입력했습니다 다시 입력하세요
#ver1 왼쪽정렬 이등변삼각형
#ver2 마름모 대칭
#ver3 사각형안에  출력될수있게.
a=0
B=" "
S="*"
while True:
    a = int(input("홀수를 입력하세요(0입력시 종료): "))
    if a==0:
        break
    if a%2 == 0:
        print("짝수를 입력했습니다. 다시 입력하세요")
        continue
    else:
        SC = 1
        BC = int((a - SC)/2)
        while True:
            print(BC*B,end="")
            print(SC*S)
            if SC == a:
                break

            SC= SC+2
            BC= BC-1



            #BC = int(a/2)
            #print(BC)
            #if BC > 3:
            #    break
            #BC = BC +1
            #SC = a
            #print(a)
            #print("&"*BC, end="")
            #print("*"*SC)
            #if SC== 10:
            #    break
            #SC = SC +1