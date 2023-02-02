# 예외처리
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 예외 반드시 처리, 로그는 반드시 남김, 예외는 던져짐, 예외 무시

# SyntaxError
# print('error)
# print('Error' ...

# NameError
a = 10
b = 15
# print(c)

# ZeroDivisionError
print(100/0)

# IndexError
x = [50, 70, 90]
print(x[1])
print(x[5])

# KeyError
dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
print(dic['Hobby'])
print(dic.get('Hobby')) # None

# 예외가 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
print(time.time2())

# ValueError
x = [10, 50, 90]
x.remove(50)
print(x)
x.remove(200)

FileNotFoundError
f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행할 경우
x = [1, 2] # List
y = (1, 2) # Tuple
z = 'test' # Text

# print(x + y)
print(x + list(y))
print(tuple(x) + y)

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# Except : 에러명1: 여러개 가능
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found It! {} in name'.format(z, x + 1)) # Kim Found It! 1 in name
except ValueError:
    print('Not Found It! - Occurred ValueError!')
else:
    print('Ok! else.') # Ok! else.

# 모든 에러 예외 처리
try:
    z = 'Lee'
    x = name.index(z)
    print('{} Found It! {} in name'.format(z, x + 1))
except Exception: # except: 도 가능
    print('Not Found It! - Occurred ValueError!')
else:
    print('Ok! else.') # Ok! else.

try:
    z = 'Choe'
    x = name.index(z)
    print('{} Found It! {} in name'.format(z, x + 1)) # Kim Found It! 1 in name
except Exception as e:
    print(e) # 'Choe' is not in list
    print('Not Found It! - Occurred ValueError!') # Not Found It! - Occurred ValueError!
else:
    print('Ok! else.')
finally:
    print('Ok! finally!') # Ok! finally!

# 예외발생 : raise => 직접 예외발생
try:
    a = 'Park'

    if a == 'Kim':
        print('Ok! Pass~!')
    else:
        raise ValueError
except ValueError:
    print('Occurred! Exception!') # Occurred! Exception!
else:
    print('Ok! Else~!')