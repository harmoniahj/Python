# External Functions (외장함수)
# sys, pickle, shutil, temfile, time, random...

# sys
import sys
print(sys.argv)

# 강제종료
# sys.exit()

# 파이썬 패키지 위치
print(sys.path)

# pickle : 객체파일 쓰기 = 읽을수 있는 데이터타입을 파일로 쓸수 있음
import pickle

# 쓰기
f = open("test.obj", 'wb')
obj = {1: 'puthon', 2: 'study', 3: 'basic'}
pickle.dump(obj, f)
f.close()

# 읽기
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()

# os : 환경변수, 디렉토리(파일) 처리 관련 운영체제 작업관련
# mkdir, rmdir(비어있으면 삭제), rename
import os
print(os.environ)
print(os.environ["USERNAME"])

# 현재 경로
print(os.getcwd())

# time : 시간 관련처리
import time

print(time.time()) # 1675318813.3753302
print(time.localtime(time.time())) # time.struct_time(tm_year=2023, tm_mon=2, tm_mday=2, tm_hour=15, tm_min=20, tm_sec=13, tm_wday=3, tm_yday=33, tm_isdst=0)
print(time.ctime()) # Thu Feb  2 15:20:52 2023
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) # 2023-02-02 15:22:20

# 시간간격 발생
# for i in range(5):
#     print(i)
#     time.sleep(1) # 초단위

# random : 난수 리턴
import random

print(random.random()) # 0 ~ 1 실수
print(random.randint(1, 45)) # 40
print(random.randrange(1, 45)) # 1~44 실수

# 섞기
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d) # [3, 2, 4, 1, 5]

#  무작위 선택
c = random.choice(d)
print(c) # 1

# webbrowser : 본인 OS의 웹브라우저 실행
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")