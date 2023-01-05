# print 사용법

# 기본 출력
print('Python Start') # Python Start
print("~!~!") # ~!~!
print('''Python Start''') # Python Start
print("""~!~!""") # ~!~!

# Separator
print('P', 'y', 't', 'h', 'o', 'n', sep = '') # Python
print('P', 'y', 't', 'h', 'o', 'n', sep = '|') # P|y|t|h|o|n
print('010', '1234', '5678', sep = '-') # 010-1234-5678

# End
print('Welcome to', end = ' ') # 다음 print문 이어줌
print('IT News', end = ' ') # Welcome to IT News
print('web Site') # Welcome to IT News web Site

# File
import sys
print('Learn Python', file = sys.stdout)

#Format (d(정수) : 3, s(문자열) : 'Python', f(실수) : 3.14454)
# %s
print('%s %s' % ('one', 'two')) # one two
print('{} {}'.format('three', 'four')) # three four
print('{1} {0}'.format('one', 'two')) # two one

print('%10s' %('Have')) # 10 : 총자리수       Have -> 왼쪽부터 공백
print('{:>10}'.format('A')) #          A

print('%-10s' %('Good')) # Good       -> 오른쪽을 공백
print('{:<10}'.format('Day')) # Day


print('{:_>10}' .format('~!')) # ________~!
print('{:^10}'.format('Day')) #    Day    -> 중앙으로 정렬

print('%.5s' %('Hi')) # Hi
print('%.5s' %('Hi My Name is JHJ')) # Hi My -> 5글자만 출력
print('{:10.5}'.format('Today Python Study')) # Today 

# %d
print('%d %d' %(1, 2)) # 1 2
print('{} {}' .format(1, 2)) # 1 2

print('%4d' % (45)) #   45
print('{:4d}'.format(42)) #   45

# %f
print('%f' % (3.1415)) # 3.141500
print('%1.18f' % (1.23456789123456789)) # 1.234567891234567893 -> 소수점 잘려서 나옴

print('%06.2f' % (3.141592653589793)) # 003.14 -> 정수부는 6자리, 소수부는 2자리 => 총자릿수 지정
print('{:06.2f}' .format(3.141592653589793)) # 003.14