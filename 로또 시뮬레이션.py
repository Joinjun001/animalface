# 로또 시뮬레이션

# 당첨 번호 하나를 먼저 만든다.
# 무작위로 생성된 번호를 만든다.
# 1등이 되려면 얼마나 많이 로또를 구매해야 되는지 구한다.

# 로또번호는 1부터 45까지, 일치 6개 > 1등  2등은 당첨번호 5개 + 보너스 숫자 일치
# 지난번 로또 당첨금인 1등에겐 27억 지급, 2등에겐 5천만원 지급, 3등에겐 160만원 지급이라 하자.
# 4등은 5만원 5등은 5천원.

# *** 요컨데 앞에서부터 순서대로 확인하면서, 같은 숫자가 있는지 체크하면서 와야됨.
# 연속으로 같아야 되는게 아닌, 같은 숫자가 몇개 있느냐기 때문,,,
# 그렇기 때문에 스텍을 쌓을 변수하나가 필요함. ***

# 위에 별표 표시한 내용은 앞으로 리스트내에서 같은 요소가 몇개 있는지 확인할때 중요한 테크닉,,
from random import *

lotto = []

for i in range(7):
    lotto.append(randrange(1,46))

print("로또 번호 :", lotto)

num = int(input("몇개의 로또를 사시겠습니까?"))

# 마지막 번호는 보너스 번호
# 이제 while문을 만들어서 반복하자.

myLotto = []

prize = 0 # 상금
cost = 0
same = 0 # 로또번호 같은 숫자 몇개 있는지 저장할 변수 최대 6개까지만, 보너스번호 제외
bonus = 0 # 보너스 번호가 맞는지 저장할 변수.


for i in range(num): # 로또 산 개수만큼 반복.
    same = 0
    cost += 1000
    myLotto = []
    for i in range(7): # 로또 번호 생성
        myLotto.append(randrange(1,46)) 

    for i in range(6): # 로또 번호 일치 개수
        if myLotto[i] == lotto[i]:
            same += 1

    if myLotto[6] == lotto[6]: # 보너스 일치인지 확인 
        bonus += 1

    if same == 3:
        prize += 5000
        print("5등 당첨번호 : ", myLotto)

    elif same == 4:
        prize += 50000
        print("4등 당첨번호 : ", myLotto)

    elif same == 5:
        prize += 1643463
        print("3등 당첨번호 : ", myLotto)

    elif same == 5 and bonus == 1:
        prize += 57201623   
        print("2등 당첨번호 : ", myLotto)

    elif same == 6:
        prize += 2745677875
        print("1등 당첨번호 : ", myLotto)

print("로또 {}개를 산 결과 당첨금은 {}이고, 비용은 {}입니다.".format(num, prize, cost))





    

