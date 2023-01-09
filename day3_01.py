# List : 순서 O, 중복, 수정, 삭제 가능
a = []
b = list()
c = [5, 10, 15, 20, 25]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [100, 1000, ['Ace', 'Base', 'Captine']]
f = [21.43, "footbar", 3, 4, True, 3.14159]

# 인덱싱
print('d =', type(d), d) # d = <class 'list'> [1000, 10000, 'Ace', 'Base', 'Captine']
print('d[1] =', d[1]) # d[1] = 10000
print('d[0] + d[1] + d[1] =',d[0] + d[1] + d[1]) # d[0] + d[1] + d[1] = 21000
print('d[-1] =]', d[-1]) # d[-1] =] Captine

print('e[-1][1] =', e[-1][1]) # e[-1][1] = Base
print('e[-1][1] =', list(e[-1][1])) # e[-1][1] = ['B', 'a', 's', 'e']

# 슬라이싱
print('d[0:3] =', d[0:3]) # d[0:3] = [1000, 10000, 'Ace']
print('d[2:] = ', d[2:])

print('e[-1][1:3] =', e[-1][1:3]) # e[-1][1:3] = ['Base', 'Captine']
# > 맨 끝에서 ['Ace : [0]', 'Base : [1]', 'Captine [3]']이므로...

# 리스트 연산
print('c + d =', c + d) # c + d = [5, 10, 15, 20, 25, 1000, 10000, 'Ace', 'Base', 'Captine']
print("c * 3 =", c * 3) # c * 3 = [5, 10, 15, 20, 25, 5, 10, 15, 20, 25, 5, 10, 15, 20, 25]
print("Test + str(c[0]) =", 'Test' + str(c[0])) # Test + str(c[0]) = Test5

# 값 비교
print('c == c[:3] + c[3:]', c == c[:3] + c[3:]) # c == c[:3] + c[3:] True

# Identity(id) : 어느 한쪽이 변경되어도 같은 결과값이 나옴
temp = c

print('temp =', temp,'c =', c) # temp = [5, 10, 15, 20, 25] c = [5, 10, 15, 20, 25
print('id(temp) =', id(temp), 'id(c)', id(c)) # id(temp) = 2908720421248 id(c) 2908720421248

# 리스트 수정, 삭제
c[0] = 4
c[1:2] = ['a', 'b', 'c']
c[1:2] = [['a', 'b', 'c']] #  리스트로 나옴

print('c =', c) # c = [4, 10, 15, 20, 25]
print('c =', c) # c = [4, 'a', 'b', 'c', 15, 20, 25]

c[1:3] = []
print('c =', c) # c = [4, 'c', 15, 20, 25]

del c[2] # 삭제
print('c =', c) # c = [4, 'c', 20, 25]

# 리스트 함수
a = [ 1, 2, 3, 4, 5]

print('a =', a) # a = [1, 2, 3, 4, 5]

a.append(0) # 끝 부분에 삽입시에 사용
print('a.aappend(0) =', a) # a.aappend(0) = [1, 2, 3, 4, 5, 0]

a.sort()
print('a.sort() =', a) # a.sort() = [0, 1, 2, 3, 4, 5] : 정렬

a.reverse()
print('a.reverse() =', a) # a.reverse() = [5, 4, 3, 2, 1, 0]

print('a.index(3) =', a.index(3), 'a[3] =', a[3]) # a.index(3) = 2 a[3] = 2

a.insert(2, 7)
print('a.insert(2, 7)', a) # a.insert(2, 7) [5, 4, 7, 3, 2, 1, 0]

a.remove(7)
print('a.remove(7) =', a) # a.remove(7) = [5, 4, 3, 2, 1, 0]

print('a.pop() =', a.pop()) # a.pop() = 0 > 기존 리스트에서 맨 마지막 인덱스를 출력
print('a =', a) # a = [5, 4, 3, 2, 1] > 맨 마지막을 뺀 나머지 인덱스 출력
print('a.count(4)', a.count(4)) # a.count(4) 1 > 값이 중복되거나 존재하는 지 확인

ex = [8,9]
a.extend(ex)
print('a.extend(ex) =', a) # a.extend(ex) = [5, 4, 3, 2, 1, 8, 9]

# 반복문 활용
while a:
    data = a.pop()
    print('data =', data) # > data가 비어있으면 while문 종료