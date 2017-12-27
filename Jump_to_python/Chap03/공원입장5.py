FT = 3
DT = 5
Visitor = 0
price = [0, 2000, 3000, 5000]
grade = ['유아', '어린이', '청소년', '성인', '노인']

while True:

    age = int(input("나이를 입력하세요: "))

    if age <= 3:
        print("귀하는 %s등급이며, 감사합니다. 티겟을 발행합니다." % grade[0])
        Visitor += 1
        if FT > 0 and Visitor>0 and Visitor % 7 == 0:
            FT = FT - 1
            print("축하합니다. 1주년 무료이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다")
            print("잔여무료티겟 %d장" % FT)
        if DT > 0 and Visitor>0 and Visitor % 4 == 0:
            DT = DT - 1
            print("축하합니다. 연간회원권 할인이벤트에 당첨되셨습니다. 할인 티켓을 발행합니다")
            print("잔여 할인티켓 %d장" % DT)
        continue
    elif age >= 66:
        print("귀하는 %s등급이며, 감사합니다. 티겟을 발행합니다." % grade[4])
        Visitor += 1
        if FT > 0 and Visitor>0 and Visitor % 7 == 0:
            FT = FT - 1
            print("축하합니다. 1주년 무료이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다")
            print("잔여무료티겟 %d장" % FT)
        elif DT > 0 and Visitor>0 and Visitor % 4 == 0:
            DT = DT - 1
            print("축하합니다. 연간회원권 할인이벤트에 당첨되셨습니다. 할인 티켓을 발행합니다")
            print("잔여 할인티켓 %d장" % DT)
        continue

    elif age <= 13:
        print("귀하는 %s등급이며" % grade[1])
        print("요금은 %d원입니다" % price[1])
    elif age <= 18:
        print("귀하는 %s등급이며" % grade[2])
        print("요금은 %d 원입니다" % price[2])
    elif age <= 65:
        print("귀하는 %s등급이며" % grade[3])
        print("요금은 %d 원입니다" % price[3])

    ptype = int(input("요금 유형을 선택하세요(1.현금, 2.공원 전용 신용카드): "))

    if ptype == 1:
        pay = int(input("요금을 입력하세요: "))

        if age <= 13 and pay == price[1]:
            print("감사합니다. 티겟을 발행합니다.")
        elif age <= 13 and pay < price[1]:
            print("금액이 %d 원 모자랍니다." %(price[1] - pay))
            print("입력하신 %d 를 반환합니다" % pay)
            Visitor -= 1
        elif age <= 13 and pay > price[1]:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" % (pay - price[1]))
        elif age <= 18 and pay == price[2]:
            print("감사합니다. 티겟을 발행합니다.")
        elif age <= 18 and pay < price[2]:
            print("금액이 %d 원 모자랍니다" % (price[2] - pay))
            print("입력하신 %d 를 반환합니다" % pay)
            Visitor -= 1
        elif age <= 18 and pay > price[2]:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" % (pay - price[2]))
        elif age <= 65 and pay == price[3]:
            print("감사합니다. 티겟을 발행합니다.")
        elif age <= 65 and pay < price[3]:
            print("금액이 %d 원 모자랍니다" % (price[3] - pay))
            print("입력하신 %d 를 반환합니다" % pay)
            Visitor -= 1
        elif age <= 65 and pay > price[3]:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" % (pay - price[3]))

    elif ptype == 2:
        if 3 <= age <= 13:
            print(" %d 원 결제 되었습니다. 티켓을 발행합니다." % (price[1] * 0.9))
        elif 14<= age <= 18:
            print(" %d 원 결제 되었습니다. 티켓을 발행합니다." % (price[2] * 0.9))
        elif age >= 19 and age <= 59:
            print(" %d 원 결제 되었습니다. 티켓을 발행합니다." % (price[3] * 0.9))
        elif 60 <= age <= 65:
            print(" %d 원 결제 되었습니다. 티켓을 발행합니다." % ((price[3] * 0.9) * 0.95))
    Visitor +=1

    if FT > 0 and Visitor>0 and Visitor % 7 == 0:
        FT = FT - 1
        print("축하합니다. 1주년 무료이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다")
        print("잔여무료티겟 %d장" % FT)
    elif DT > 0 and Visitor>0 and Visitor % 4 == 0:
        DT = DT - 1
        print("축하합니다. 연간회원권 할인이벤트에 당첨되셨습니다. 할인 티켓을 발행합니다")
        print("잔여 할인티켓 %d장" % DT)
