
# better = int(input("your?"))
# print(f"너는 {better}을 입력했다")

# if better >= 1000:
#     print("수익이다")
# else:
#     print("적자다")


# 휴대폰 = int(input("너의 공부량은?"))

# print(f"너는 휴대폰 사용량이 {휴대폰}이다")

# if 휴대폰 >=10:
#     print("휴대폰 잠금해제")
# elif 휴대폰 >=5:
#     print("휴대폰 30분 사용가능")
# else:
#     print("나머지 불가능")

# 현재_갖고있는_금액 = int(input("넌 얼마 갖고있지?"))
# print(f"{현재_갖고있는_금액} 원 갖고 있음")

# if 현재_갖고있는_금액>=20000:
#     print("치킨 가능")
# elif 현재_갖고있는_금액 >=10000:
#     print("떡볶이")
# else:
#     print("편의점 김밥")


#리스트 
# animals = ["가물치", "하마","비단뱀","도룡뇽"]

# empty = []

# print(animals[2])
# print(animals[-1])

# animals.append("고라니")
# print(animals)

# #데이터 할당
# animals[1] = "청개구리"
# print(animals)

# del animals[0]
# print(animals)

# #슬라이싱
# print(animals[1:3])


# result = [33,40,12,63,52]

# result.append(9)
# print(result)

# result[1]=50
# print(result)

# print(result[2:6])

# result.sort()
# print(result)

# data=[]

# x = int(input("1일차 턱걸이 횟수"))
# data.append(x)

# x = int(input("2일차 턱걸이 횟수"))
# data.append(x)

# total = data[0] + data[1]

# avg = total / 2

# print(avg)


#반복문 
# data = []

# for i in range(1, 101):
#     x=int(input(i,"턱걸이 일차"))
#     data.append(x)

# print(x)

# for a in [1,2,3,4]:
#     print(a)

# range(10) #0~9까지 숫자 포함하는 range 객체를 만들어준다.

# champions = ["티모","이즈리얼","리신"]

# for champion in champions:
#     print("챔피언은",champion, "입니다")

# #문자열사용
# fighting_message = "화이팅"

# for word in fighting_message:
#     print(word)



#range 객체 사용 


# for i in range(1, 10,2 ):
#     print(i)

#while 사용
# i=0
# while i < 10:
#     print(i, "번 다짐, 나는 할수있다")
#     i+=1


# 구구단 = int(input("몇단을 입력할까?"))
# print(f"{구구단}을 입력했다")

# for i in range(1, 10):
#     print(구구단, "*", i, "=", 구구단*i)


# while True:
#     print("[메뉴를 입력하세요]")
#     select = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료"))
#     if select == 1:
#         print("게임을 시작하다")

#     elif select==2:
#         print("실시간 랭킹")
#     elif select==3:
#         print("게임 종료")
#         break
#     else:
#         print("다시 입력")


# word_list = ["test1", "test2", "test3"]

# 점수 = 0


# for word in word_list:
#     print(word)
#     data = input()
#     if data == word:
#         점수 += 1 #맞추면 점수 1증가

# print("전체 문제갯수 : ", len(word_list))
# print("맛힌 갯수:", 점수)
# print("점수 :", len(word_list)-점수)


# def add(a, b):
#     result = a + b
#     return result
# print(add(5,6))

# import random
# def getRandomNumber():
#     number = random.randint(1,45)
#     return number
    
# lotto_num = [] #로또 저장할 리스트 

# for i in range(6):
#     random_number = getRandomNumber()
#     lotto_num.append(random_number)

# lotto_num.sort()

# for num in lotto_num:
#     print(num, end = " ")

import random
def getRandomNumber():
    number = random.randint(1,45)
    return number
    
lotto_num = [] #로또 저장할 리스트 

count = 0

while True:
    if count > 5:
        break
    random_number = getRandomNumber()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count +=1

lotto_num.sort()

for num in lotto_num:
    print(num, end = " ")


