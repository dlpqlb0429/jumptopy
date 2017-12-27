price= [0, 2000, 3000, 5000]
grade= ['유아', '어린이', '청소년', '성인', '노인']
while True:

        age = int(input("나이를 입력하세요: "))
        if age <=3:
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

        pay = int(input("요금을 입력하세요: "))

        if age <=13 and pay == price[1]:
                print("감사합니다. 티겟을 발행합니다.")

        elif age <= 13 and pay < price[1]:
            print("금액이 %d 원 모자랍니다" % (price[1] - pay))
            print("입력하신 %d 를 반환합니다" % pay)
        elif age <=13 and pay > price[1]:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(pay-price[1]))

        elif age <=18 and pay == price[2]:
            print("감사합니다. 티겟을 발행합니다.")
        elif age <=18 and pay < price[2]:
            print("금액이 %d 원 모자랍니다" % (price[2] - pay))
            print("입력하신 %d 를 반환합니다" % pay)
        elif age <= 18 and pay > price[2]:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(pay-price[2]))


        continue
