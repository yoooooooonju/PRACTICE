print(5)
print(-10)
print(3.141592)
print(1000000)
print(5+3+2)
print(3*7)
print (3*(3+4))

print('새신을신고뛰어보자')
print("뛰지말고날아가보자")
print("ㅋ"*10)

# boolean은 참과 거짓을 나타냄
print(5>10)
print(5<10)
print(True)
print(not True)
print(not (5>10))


# about 변수 // 우리집강아지딸기

animal = "강아지"
name = "딸기"
age = 13
like = "사과"
is_grandma = age >= 10


print("우리집 "+ animal +"는 " + name + "야")
like = "공놀이" #왜 사과 말고 이게 실행되는 거지? 가까운거에 영향을 받는건가
print(name +"는 "+ str(age)+"살이고, "+ like +"을 좋아해요")
print(name +"는 할머니일까요? "+ str (is_grandma))
#모든 것에 +를 제대로 붙여줘야 하는구나! 따옴표는 문장에만ㅎ // 아 +를 ,로 바꿔도 ㅇㅋ이네 ,일 땐 정수에 str 없어도 ㄱㅊ

# 변수명은 station으로, 변수값은 "사당", "신도림", "인천공항" 순서대로 입력, 출력문장은 "XX행 열차가 들어오고 있습니다

XX = "사당" # 근데 이걸 XX말고 station이라고 하는 편이 더 좋았으려나...

print(XX+"행 열차가 들어오고 있습니다")

#연산자

print(1+1)
print(5*4)
print(3**3) # 3^3
print(10%3) # 나머지구하기
print(5//3) #몫 구하기
print(10//3)
print(10<3) #ture or false
print(10<=9)

print(3==4) #앞에 있는 값과 뒤에 있는 값이 똑같은지 확인하는 것
print(3+5==6)

print(1 != 3) #앞뒤가 같지 않은지 확인하는 것. 여기서는 true임
print(not(1!=3)) #not true 이니까 false

print((3>0) and (3<5)) # 둘 다 맞는지 확인하는 것. 여기서는 true (둘 다 맞을 때)
print((3 > 0) & (3 < 5)) # & = and

print((3>0) or (3>5)) #둘 중 하나만 맞아도 true
print((3>0) | (3>5)) #or = |

print(3>2>5) #false

#수식
print(2+3*4) #14
print((2+3)*4) #20
number = 2+3*4
print(number)
number = number+2
print(number) #얘네는 쭉 아래로만 가나보다
number += 2 #이건 number = number + 2 를 줄여서 쓴 말이라네
number *= 2
print(number)
number /= 2
print(number)

number %= 2 # 18을 2로 나눴을 때의 나머지. 0이겠지
print(number)


#숫자처리함수

print(abs(-5)) #절댓값
print(pow(4,2)) # 4^2를 뜻함
print(max(5,12)) # 최댓값. 5랑 12중에 뭐가 더 크냐
print(min(5,11)) # 최솟값
print(round(3.14)) #반올림

from math import * #math 라이브러리 안에 있는 모든 걸 이용하겠다는 뜻이라네
print(floor(4.99)) #내림
print(ceil(4.89)) #올림
print(sqrt(16)) #제곱근

#랜덤함수. 난수 무작위로 뽑아주는 것
from random import *
print(random()) #숫자가 정말 마구잡이로 나오는군... (0.0,1.0)
print(random()*10) #0.0~10.0
print(int(random()*10)) #int로 감싸줘서 정수로 살림
print(int(random()*10))
print(int(random()*10)+1) #1~10 중 임의의 값 생성 가능
print(int(random()*50)+1) #1~50 중 임의의 값 생성 가능

print(randrange(1,45)) # 1~45 미만의 임의의 값 생성. 45도 나오게 하고 싶으면 46을 넣어야 함
print(randint(1,45)) #1~45이하의 임의의 값 생성.

#퀴즈! 월 4회 스터디, 3번은 온라인 1번은 오프라인. 모임 날짜를 정해주는 프로그램 만들기
# 조건 1: 랜덤, 2: 월별 날짜 28일, 조건 3: 1~3일은 제외

from random import *
#print(randint(4,28)) 난 이지랄햇는데......
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" +str(date)+ "일로 선정되었습니다 ")


