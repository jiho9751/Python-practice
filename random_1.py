from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1)

print(int(random() * 45) + 1) #1~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) #1~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) #1~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) #1~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) #1~ 45 이하의 임의의 값 생성
print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성

date = randrange(4,29)
#print("오픈라인 스터디 모임 날짜는 매월 "+ str(date) +"일로 선정되었습니다.")