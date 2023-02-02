# Built-in Functions (내장함수)

# 절대값
print(abs(-3)) # 3

# all= > and, any => or : iterable 요소 검사(참, 거짓)
print(all([1, 5, 10])) # True
print(all([1, 2, 0])) # False
print(all([1, 2, ''])) # False

print(any([1, 2, 0])) # True

# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(72)) # H
print(ord('J')) # 74

# enumerate : 인데스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -5, 3, -53, 0]))) # [-5, 3, -53]
print(list(filter(lambda x: abs(x) > 2, [1, -2, 10, -5, 0]))) # [10, -5]

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(4))) # 140725953291144
print(id(5)) # 140725953291176

# len :요소의 길이 반환
print(len('abcdefg')) # 7
print(len([1, 2, 3, 4, 5, 6, 7])) # 7

# max, min : 최대값, 최소값
print(max([1, 5, 3])) # 5
print(max('Python Study~!')) # ~
print(min([5, 2, 3])) # 2

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1, -3, 2, 0, -5, 8]))) # [1, 3, 2, 0, 5, 8]
print(list(map(lambda x:abs(x), [1, -3, 2, 0, -5, 8]))) # [1, 3, 2, 0, 5, 8]

# pow : 제곱값 반환
print(pow(2, 10)) # 1024

# range : 반복가능한 객체(Iterable) 반환
print(range(1, 10, 2)) # range(1, 10, 2)
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]
print(list(range(1, -10, -2))) # [1, -1, -3, -5, -7, -9]

# round : 반올림
print(round(6.5781, 2)) # 6.58
print(round(3.14125, 4)) # 3.1412

# sorted : 반복가능한 객체(Iterable) 정렬 후 반환
print(sorted([6, 7, 4, 10, 1])) # [1, 4, 6, 7, 10]

a = sorted(['p','y', 't', 'h', 'o', 'n'])
print(a)

# sum : 반복가능한 객체 합 반환
print(sum([1, 5, 6, 9, 10])) # 31
print(sum(range(1, 101))) # 5050

# type : 자료형 확인
print(type(3)) # <class 'int'>
print(type({})) # <class 'dict'>
print(type({2, 5})) # <class 'set'>

# zip : 반복가능한 객체의 요소를 묶어서 반환 => tuple로 묶어서...
print(list(zip([10, 20, 30], [40, 50, 60]))) # [(10, 40), (20, 50), (30, 60)]
print(list(zip([10, 20, 30], [50, 60]))) # [(10, 50), (20, 60)]