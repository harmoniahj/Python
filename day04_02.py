# while문 : 조건이 만족하는 동안 계속 반복
# while <expression>:
#   <statement(s)>
n = 5
while n > 0:
    n = n-1
    print(n)

a = ['foo', 'bar', 'baz']
while a:
    print('a.pop() =', a.pop(-1))

# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print('n :', n)
print('Loop End')

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print('m :', m)
print('Loop End')

# if 중첩
i = 1
while i <= 10:
    print('i :', i)
    if i == 6:
        break
    i += 1

# while - else 문
n = 10
while n > 0:
    n -= 1
    print('n :', n)
    if n == 5:
        break
else:
    print('Else out!!')

a = ['foo', 'bar', 'bz', 'qux']
s = 'Kim'
i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'Not Found in List')

a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print('a.pop() :', a.pop())