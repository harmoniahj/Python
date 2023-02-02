# Sets (집합) : 순서 / 중복 X, 
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a =', a, 'type(a) =', type(a)) # a = set() type(a) = <class 'set'>
print('e =', e) # e = {'foo', 'baz', 'bar', 'qux'} > 중복 허용X

# Tuple 변환 (set -> Tuple)
t = tuple(b)

print('type(t) =', type(t), 't =', t) # t[0] = 1 t[1:3] = (2, 3)
print('t[0] =', t[0], 't[1:3] =', t[1:3]) # t[0] = 1 t[1:3] = (2, 3)

# List 변환 (set -> List)
l = list(c)
l2 = list(e)

print('l =', l) # l = [1, 4, 5, 6]
print('len(l) =', len(l)) # len(l) = 4

# 집합 자료형
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 =', s1 & s2) # s1 & s2 = {4, 5, 6} > 교집합 출력
print('s1.intersection(s2) =', s1.intersection(s2)) # s1.intersection(s2) = {4, 5, 6}

print('s1 | s2 =', s1 | s2) # s1 | s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('s1.union(s2) =', s1.union(s2)) # s1.union(s2) = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print('s1 - s2 =', s1 - s2) # s1 - s2 = {1, 2, 3}
print('s1.difference(s2) =', s1.difference(s2)) # s1.difference(s2) = {1, 2, 3}

# 중복된 원소 확인
print('s1.isdisjoint(s2) =', s1.isdisjoint(s2)) # s1.isdisjoint(s2) = False > 교집합이 있음

# 부분집합 확인
print('s1.issubset(s2) =', s1.issubset(s2)) # s1.issubset(s2) = False
print('s2.issuperset(s) =', s2.issuperset(s1)) # s2.issuperset(s1) = False

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1.add(5) =', s1) # s1.add(5) = {1, 2, 3, 4, 5}

s1.remove(3)
print('s1.remove(3) =', s1) # s1.remove(3) = {1, 2, 4, 5}

s1.discard(2) # 에러 발생 X
print('s1.discard(2) =', s1) # s1.discard(2) = {1, 4, 5}

s1.clear()
print('s1.clear() =', s1) # s1.clear() = set()