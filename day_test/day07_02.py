# Hangman 미니게임2
import time
import csv # CSV 처리
import random
import winsound

name = input("What is your name?? ")

print("Hi, " + name, "Time to Play Hangman Game~!")

print()

time.sleep(1)

print("Strart Loading...")
print()
time.sleep(0.5)

# CSV 단어 리스트
words = []

with open('resource/word_list.csv', 'rt', encoding='UTF8') as f:
	reader = csv.reader(f)

	# Header Skip
	next(reader)

	for c in reader:
		words.append(c)

# 리스트 섞기
random.shuffle(words)
# 임의의 단어 선택
q = random.choice(words)

word = q[0].strip() #정답 단어
guesses = ''
turns = 7 # 남은 기회

while turns > 0:
    failed = 0

    # 정답 단어 반복 
    for char in word:
        if char in guesses: # 정답 단어에 추측 문자가 포함되어 있는 경우
            print(char, end = '')
        else:
            print("_", end = ' ') # 틀린 경우에 _ 로 표시
            failed += 1
        
    print()
        
    if failed == 0: # 단어가 맞을 경우
        print()
        winsound.PlaySound('sound/good.wav', winsound.SND_FILENAME) # 성공 소리
        print('Congratulations~! The Guesses is correct.')
        break # while 구문 중단

    print('Hint : {}'.format(q[1].strip()))
    guess = input("guess a charater : ") # 추축한 단어 문자 단위 입력
    print()

    guesses += guess # 단어 더함

    if guess not in word: # 정답 단어에 추축한 문자가 포함되어 있지 않으면..
        turns -= 1
        winsound.PlaySound('./sound/bad.wav',winsound.SND_FILENAME) # 실패 소리
        print("Oops! Wrong Word") # 오류 메시지
        print("You Have", turns, 'more guesses!!') # 남은 기회 출력
        print()

        if turns == 0:
            print("You Hangman Game Failed. Bye~!")