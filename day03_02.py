# Tuple : 순서, 중복 O / 수정, 삭제 X > 불변
a = ()
b = (1,)
b_1 = (1)
c = (10, 20, 30, 40)
d = (100, 1000, 'Ace', "Base", 'Captine')
e = (100, 1000, ('Ace', "Base", 'Captine'))

print('type(b) =', type(b), 'type(b_1) =', type(b_1)) # type(b) = <class 'tuple'> type(b_1) = <class 'int'>

# 인덱싱
print('d[1] =', d[1]) # d[1] = 1000
print('d[0] + d[1] =', d[0] + d[1]) # d[0] + d[1] = 1100
print('e[-1] =', e[-1]) # e[-1] = ('Ace', 'Base', 'Captine')
print('list(e[-1]) =', list(e[-1])) # list(e[-1]) = ['Ace', 'Base', 'Captine'] > list로 형변환

# d[0] = 1500 > TypeError: 'tuple' object does not support item assignment

# 슬라이싱
print('d[0:3 =', d[0:3]) # d[0:3 = (100, 1000, 'Ace')
print('e[2][1:3] =', e[2][1:3]) # e[2][1:3] = ('Base', 'Captine')

# Tuple 연산
print('c + d =', c + d) # c + d = (10, 20, 30, 40, 100, 1000, 'Ace', 'Base', 'Captine')
print('c * 3 =', c * 3) # c * 3 = (10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40)

# 함수
a = (5, 2, 1, 3, 4)
print('a.index(3) =', a.index(3)) # a.index(3) = 3
print('a.count(3) =', a.count(3)) # a.count(3) = 1

# Packing & Unpacking
# Packing
t = ('one', 'two', 'three', 'four')

print(' t =', t) #  t = ('one', 'two', 'three', 'four')
print('t[0]', t[0]) # t[0] one
print('t[-1]', t[-1]) # t[-1] four

# Unpacking : 풀어서 각각 할당함
(x1, x2, x3, x4) = t # = x1, x2, x3, x4 = t
print('type(x1) =', type(x1), 'type(x2) =', type(x2), 'type(x3) =', type(x3), 'type(x4) =', type(x4))
# type(x1) = <class 'str'> type(x2) = <class 'str'> type(x3) = <class 'str'> type(x4) = <class 'str'>
print('x1 =', x1, 'x2 =', x2, 'x3 =', x3, 'x4 =', x4) # 1 = one x2 = two x3 = three x4 = four

t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
(x4, x5, x6) = 4, 5, 6

print('t2 =', t2)
print('x4 =', x4, 'x5 =', x5, 'x6 =', x6) # x4 = 4 x5 = 5 x6 = 6