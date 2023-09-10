sentence = '나는 윤주다'
print(sentence)
sentence2 = "나는 이윤주다"
print(sentence2)
sentence3 = """나는 이윤주고
지금 공부중이다
"""
print(sentence3)

#슬라이싱
jumin = "030331-1234567" #필요한 정보만큼 자르는 게 슬라이싱 // 맨 처음이 0

print("성별 :" +jumin[7])
print("연 :" +jumin[0:2]) #0부터 2직전까지. 즉, 0,1번째에 있는 값만 가져옴
print("월 :" +jumin[2:4])
print("일:"+jumin[4:6])
print("생년월일: " + jumin[0:6]) # 0:6 말고 그냥 :6이라고 해도 ㄱㅊ
print("주민번호 뒤 7자리:" + jumin[7:14]) # 14말고 7: 이렇게 해도 됨. 7부터 끝까지를 뜻함
print("주민번호 뒤 7자리 (근데 뒤에부터):" + jumin[-7:]) #맨 뒤 7번째부터 끝까지. reverse하면 맨 뒤에를 -1이라고 함...

##문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 다 소문자가 됨
print(python.upper())
print(python[0].isupper()) #문장의 0번째가 대문자냐
print(len(python)) #문장의 길이가 어느 정도냐
print(python.replace("Python","java")) #문장의 단어를 다른 것으로 바꿈

index = python.index("n")
print(index) #n이 5번째 위치에 있다고

index = python.index("n",index+1) #아까 찾은 거에 하나 더한... 거지
print(index) #두번째 n은 15번째에 있다고

print(python.find("n"))
print(python.find("java")) #내가 원하는 값이 변수에 포함되어있지 않으면 마이너스 일이 나옴
# print(python.index("java") 를 하면 에러가 남.

print(python.count("n")) #문장에 n이 몇개 나오는지 세 주는 것

##문자열 포맷

#방법 1 : 나는 ~살입니다

print("나는 %d살입니다." %20) #d는... 정수만 됨
print("나는 %s을 좋아해요" %"파이썬") # %s는 문자열을 넣겠다는 것.
print("Apple은 %c로 시작해요." %"A") # %c는 글자열이라서 한 글자만 됨
# %s는 사실 다 됨.

print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간")) #괄호 순서대로 들어감

#방법 2 : 나는 ~살입니다
print("나는 {}살입니다.".format(21))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "초록"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "초록"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "초록"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))

#방법 4
age = 21
color = "초록"
print(f"나는 {age}살이며, {color}색을 좋아해요") # 변수 값을 가지고 오는 것.

#탈출문자

print("우리집 딸기가 \n 너무너무 귀여워") #줄을 바꿔줌
# print("저는 "이윤주"입니다")
print("저는 '이윤주'입니다")
print('저는 "이윤주"입니다')
print("저는 \"이윤주\"입니다.") #역슬러시가 따옴표를 냅둬줌

# \\ : 문장 내에서 \로 바뀌게 됨  ?????
#print("http\:instagram\"lumooos")


# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #파인애플이 나와야 한다는데 난 왜 파인만 나오지....

# \b :백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

#퀴즈... 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오 규칙 1: http 부분 제외. 2: .이후 제외 3: 남은 글자 중 첫 세자리 +글자 갯수+글자 내 'e'갯수, "!"로 구성

#password = "http://naver.com"
#print(password[7:12])
#print(password[7:10])+(len(password))

# print(password[7:9]+len(password)+password.count("e")+"!") 아이고 이걸 요지경으로 하면 안되지

url = "http://google.com"
bfpassword = url.replace("http://"," ")
print(bfpassword)
# bfpassword = bfpassword[:bfpassword.index(".")]
bfpassword = bfpassword.replace(".com"," ")
print(bfpassword)

password = bfpassword[0:3]+str(len(bfpassword))+str(bfpassword.count("e"))+"!"
print(password)

print("{0}의 비밀번호는 {1}임".format(url,password))

