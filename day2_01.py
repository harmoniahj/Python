# 데이터타입
str = "Python"
bo = False
str1 = 'Anaconda'
flo = 10.0 # 10 (정수타입) <> 10.0 (실수타입)
i = 7

list  [str, str1]
dict = { # 사전 타입
    "name" : "Machine Learning",
    "version" : 2.0
}
tuple = (1, 2, 3) # = 1, 2, 3
set = {4, 5, 6}

print('str =', str, 'bo =', bo, 'str1 =', str1, 'flo =', flo, 'i =', i)
# <class 'str'> <class 'bool'> <class 'str'> <class 'float'> <class 'int'> <class 'type'> <class 'dict'> <class 'type'> <class 'set'>
print(type(str), type(bo), type(str1), type(flo), type(i), type(list), type(dict), type(tuple), type(set))

# 숫자형 연산자
'''
 +
 -
 *
 /
 // : 몫
 % : 나머지
 abs(x) : 절대값
 pow(x, y) = x ** y : x의 y 제곱
'''

# 정수 선언
i = 77
i2 = -15
big_int = 123456789123456789123456789

print('i =', i, 'i2 =', i2, 'big_int =', big_int) # i = 77 i2 = -15 big_int = 123456789123456789123456789

# 실수 선언
f = 0.123456
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print('f =', f, 'f2 =', f2, 'f3 =', f4, 'f3 =', f4) # f = 0.123456 f2 = 3.141592 f3 = 0.3333333333333333 f3 = 0.3333333333333333

# 연산
i = 39
i2 = 939
bigInt = 123456789123456789123456789
bigInt2 = 987654321987654321987654321
f1 = 1.234
f2 = 3.939

# +
print("i + i2 =", i + i2) # i + i2 = 978
print("bigInt + bigInt2 =", bigInt + bigInt2) # bigInt + bigInt2 = 1111111111111111111111111110
print("f1 + f2 =", f1 + f2) # f1 + f2 = 5.173

# *
print("i * i2 =", i * i2) # i * i2 = 36621
print("f1 * f2 =", f1 * f2) # f1 * f2 = 4.860726

# 형 변환
a = 3. # 3.0 에서 0 생략가능
b = 6
c = .7
d = 12.7

print('a =', a, 'b =', b, 'c =', c, 'd =', d) # a = 3.0 b = 6 c = 0.7 d = 12.7
print('b =', float(b), 'c =', int(c)) # b = 6.0 c = 0
print('int(True) =', int(True), 'int(False) =', int(False)) # int(True) = 1 int(False) = 0
print('complex(3)', complex(3), 'complex(3) =', complex('3')) # complex(3) (3+0j) complex('3') = (3+0j)

# 수치 연산 함수
print('abs(-7) =', abs(-7)) # abs(-7) = 7
x, y = divmod(100, 8)
print('x =', x, 'y =', y) # x = 12 y = 4
print('pow(5, 3) =', pow(5, 3), '5 ** 3 =', 5 ** 3) # pow(5, 3) = 125 5 ** 3 = 125

# 외부 모듈
import math

print('math.ceil(5.1) =', math.ceil(5.1)) # math.ceil(5.1) = 6 : x 이상의 수 중에서 가장 작은 정수
print('pi =', math.pi) # pi = 3.141592653589793