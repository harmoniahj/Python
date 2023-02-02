# For문
# for in <collection>
#   <loop body>
for v1 in range(10): # 0 ~ 9 출력
    print('v1 is', v1)

for v2 in range(1, 11):
    print('v2 is', v2)

for v3 in range(1, 11, 2):
    print('v3 is', v3)

# 1~1000까지의 합 구하기
sum2 = 0
for v in range(1, 1001):
    sum2 += v

print('sum2 =', sum2) # sum2 = 500500
print('sum2 =', sum(range(1, 1001))) # sum2 = 500500
print('4의 배수 합 =', sum(range(4, 1001, 4))) # 4의 배수 합 = 125500

# Iterables 자료형 반복 : 문자열, List, Tuple, Set, Dictionary
#iterable 리턴 함수 : range, enumerate, filter, map, zip

names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for n in names:
    print('You are name is', n)

lotto = [11, 19, 21, 28, 36, 37]
for n in lotto:
    print("Current number", n)

word = "Beautiful"
for s in word:
    print('Word is', s)

my_info = {
    "Name": 'Lee',
    "Age": 33,
    "City": "Seoul"
}
for key in my_info:
    print('key :', my_info[key])

for v in my_info.values():
    print('value :', v)

# 대문자로 출력
name = 'FineAppLE'
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break문
number = [14, 3, 4, 7, 10, 24, 5, 96, 57, 38, 48]

for num in number:
    if number == 10:
        print('Found :', num)
        break
    else:
        print('Not Found :', num)

# continue문
lt = ["1", 2, 6, True, 3.14, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print('Current Type is', type(v))

# for else
number = [14, 3, 4, 7, 10, 24, 5, 96, 57, 38, 48]

for num in number:
    if num == 7:
        print('Found :', num)
        break
else:
    print('Nout Found : 7')

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        # print(i, '*', j, '=', i * j)
        print("{:4d}".format(i * j), end='')
        print()

# 변환 예제
name2 = 'Aceman'

print('reversed :', reversed(name2)) # reversed : <reversed object at 0x000002484FE1FF40>
print('List :', list(reversed(name2))) # List : ['n', 'a', 'm', 'e', 'c', 'A']
print('Tuple :', tuple(reversed(name2))) # Tuple : ('n', 'a', 'm', 'e', 'c', 'A')
print('Set :', set(reversed(name2))) # Set : {'e', 'c', 'n', 'A', 'a', 'm'} => 순서 없음