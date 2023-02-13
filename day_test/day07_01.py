# Hangman 미니게임
import time

name = input("What is your name?? ")

print("Hi, " + name, "Time to Play Hangman Game~!")

print()

time.sleep(1)

print("Strart Loading...")
time.sleep(0.5)

word = 'secret'
guesses = ''
turns = 5 # 남은 기회

while turns > 0:
    failed = 0

    # 정답 단어 반복 
    for char in word:
        if char in guesses: # 정답 단어에 추측 문자가 포함되어 있는 경우
            print(char, end = '')
        else:
            print("_", end = ' ') # 틀린 경우에 _ 로 표시
            failed += 1
        
    if failed == 0: # 단어가 맞을 경우
        print()
        print('Congratulations~! The Guesses is correct.')
        break

    print()

    guess = input("guess a charater : ") # 추축한 단어 문자 단위 입력

    guesses += guess # 단어 더함

    if guess not in word: # 정답 단어에 추축한 문자가 포함되어 있지 않으면..
        turns -= 1
        print("Oops! Wrong Word") # 오류 메시지
        print("You Have", turns, 'more guesses!!') # 남은 기회 출력
        print()

        if turns == 0:
            print("You Hangman Game Failed. Bye~!")