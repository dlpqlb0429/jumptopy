#<특별 연습문제4>
#나이를 입력 받아 나이에 따른 대구 IT공원 등급,입장료를 계산 하는 프로그램을 작성하시오.

#0~3세(유아):무료
#4~13세(어린이): 2000원
#14~18세(청소년): 3000원
#19~65세(성인): 5000원
#66세 이상(노인): 무료

#[화면 출력]
#나이를 입력하세요.
#귀하는 []등급이며 요금은 []원 입니다.

#요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드)
#   ptype = int(intput("요금 유형을 선택하세요."))

#1. 현금인 경우
#요금을 입력하세요.
#(금액 미만 일 경우: "[]가 모자랍니다. 입력 하신 []를 반환합니다."
#금액이 일치하는 경우: "감사합니다. 티켓을 발행합니다."
#금액을 초과하는 경우: "감사합니다. 티켓을 발행하고 거스름돈 []를 반환 합니다."

#2. 공원 전용 신용 카드
#(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)
#  []원 결제 되었습니다. 티켓을 발행합니다.

price= [0, 2000, 3000, 5000]
grade= ['유아', '어린이', '청소년', '성인', '노인']
while True:

    age = int(input("나이를 입력하세요: "))
    if 0 <= age <=3:
        print("귀하는 %s등급이며, 감사합니다. 티겟을 발행합니다." %grade[0])
        continue
    elif age >= 66:
        print("귀하는 %s등급이며, 감사합니다. 티겟을 발행합니다." % grade[4])
        continue

    elif age <=13:
        print("귀하는 %s등급이며" % grade[1])
        print("요금은 %d원입니다" % price[1])
    elif age <=18:
        print("귀하는 %s등급이며" % grade[2])
        print("요금은 %d 원입니다" % price[2])
    elif age <=65:
        print("귀하는 %s등급이며" % grade[3])
        print("요금은 %d 원입니다" %price[3])

    ptype = int(input("요금 유형을 선택하세요(1.현금, 2.공원 전용 신용카드): "))

    if ptype == 1:

        pay = int(input("요금을 입력하세요: "))

        if age <=13 and pay == price[1]:
            print("감사합니다. 티겟을 발행합니다.")

        elif age <=13 and pay < price[1]:
            print("금액이 %d 원 모자랍니다" % (price[1] - pay))
            print("입력하신 %d 를 반환합니다" % pay)
        elif age <=13 and pay > price[1]:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(pay-price[1]))
        elif age <=18 and pay == price[2]:
            print("감사합니다. 티겟을 발행합니다.")
        elif age <=18 and pay < price[2]:
            print("금액이 %d 원 모자랍니다" % (price[2] - pay))
            print("입력하신 %d 를 반환합니다" % pay)
        elif age <=18 and pay > price[2]:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(pay-price[2]))
        elif age <=65 and pay == price[3]:
            print("감사합니다. 티겟을 발행합니다.")
        elif age <=65 and pay < price[3]:
            print("금액이 %d 원 모자랍니다" % (price[3] - pay))
            print("입력하신 %d 를 반환합니다" % pay)
        elif age <=65 and pay > price[3]:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" % (pay - price[3]))

    elif ptype == 2:
        if age <=3:
            print(" %d 원 결제 되었습니다. 티켓을 발행합니다." %(price[1]*0.9))
        elif age <=18:
            print(" %d 원 결제 되었습니다. 티켓을 발행합니다." % (price[2] * 0.9))
        elif age >= 19 and age <= 59:
            print(" %d 원 결제 되었습니다. 티켓을 발행합니다." % (price[3] * 0.9))
        elif 60 <= age <=65:
            print(" %d 원 결제 되었습니다. 티켓을 발행합니다." % ((price[3] * 0.9)*0.95))
        continue