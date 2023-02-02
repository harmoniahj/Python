# Dictionary : 범용적으로 많이 사용, 순서, 키 중복 X, 수정, 삭제 O
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '010203'}
b = {0:'Hello Python'} 
c = {'arr': [1, 2, 3, 4]}
d = {
    'name': 'Neceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Lee'),
    ('City', 'Jeju'),
    ('Age', 25),
    ('Grade', 'C')
])
f = dict(
    Name = 'Back',
    City = 'Seoul',
    Sge = 10,
    Grade = 'C',
    Status = False
)

'''
print('a =', a, ',', 'type(a) =', type(a)) # a = {'name': 'Kim', 'phone': '01012345678', 'birth': '010203'} , type(a) = <class 'dict'>
print('b =', b, ',', 'type(b) =', type(b)) # b = {0: 'Hello Python'} , type(b) = <class 'dict'>
print('c =', c, ',', 'type(c) =', type(c)) # c = {'arr': [1, 2, 3, 4]} , type(c) = <class 'dict'>
print('d =', d, ',', 'type(d) =', type(d)) # d = {'name': 'Neceman', 'City': 'Seoul', 'Age': 33, 'Grade': 'A', 'Status': True} , type(d) = <class 'dict'>
print('e =', e, ',', 'type(e) =', type(e)) # e = {'Name': 'Lee', 'City': 'Jeju', 'Age': 25, 'Grade': 'C'} , type(e) = <class 'dict'>
print('f =', f, ',', 'type(f) =', type(f)) # f = {'Name': 'Back', 'City': 'Seoul', 'Sge': 10, 'Grade': 'C', 'Status': False} , type(f) = <class 'dict'>
'''

print("a['name'] =", a['name']) # a['name'] = Kim
print("a.get('name') =", a.get('name')) # a.get('name') = Kim > 키 존재하지 않으면 에러 발생
print("a.get('name1') =", a.get('name1')) # a.get('name1') = None > name1이 없을 경우 None으로 출력
print('b[0] =', b[0]) # b[0] = Hello Python
print("f.get('City') =", f.get('City')) # f.get('City') = Seoul

# 추가
a['Address'] = 'Gangnam'
print('a =', a) # a = {'name': 'Kim', 'phone': '01012345678', 'birth': '010203', 'Address': 'Gangnam'}

a['Rank'] = [1, 2, 3]
print('a =', a, 'len(a) =', len(a)) # a = {'name': 'Kim', 'phone': '01012345678', 'birth': '010203', 'Address': 'Gangnam', 'Rank': [1, 2, 3]} len(a) = 5
# len() > 키의 길이

# dict_keys, dict_values, dict_items : 반복문에서 사용 가능
print('a.keys() =', a.keys()) # a.keys() = dict_keys(['name', 'phone', 'birth', 'Address', 'Rank']) > 키 값만 가져옴
print('list(e.keys()) =', list(e.keys())) # list(e.keys()) = ['Name', 'City', 'Age', 'Grade']

print('b.values() =', b.values()) # b.values() = dict_values(['Hello Python'])
print('list(f.values()) =', list(f.values())) # list(f.values()) = ['Back', 'Seoul', 10, 'C', False]

print('c.items() =', c.items()) # c.items() = dict_items([('arr', [1, 2, 3, 4])]) > 하나의 Tuple 형태로 선언됨

print("a.pop('name') =", a.pop('name')) # a.pop('name') = Kim
print('a =', a) # a = {'phone': '01012345678', 'birth': '010203', 'Address': 'Gangnam', 'Rank': [1, 2, 3]}

print("f.popitem() =", f.popitem()) # f.popitem() = ('Status', False)
print("f.popitem() =", f.popitem()) # f.popitem() = ('Grade', 'C')
print('f =', f) # f = {'Name': 'Back', 'City': 'Seoul', 'Sge': 10}

print("'birth' in a =", 'birth' in a) # 'birth' in a = True
print("'city' in d =", 'city' in d) # 'city' in d = False

# 수정
a['test'] = 'test_dict'
print('a =', a) # a = {'phone': '01012345678', 'birth': '010203', 'Address': 'Gangnam', 'Rank': [1, 2, 3], 'test': 'test_dict'}

a['Address'] = 'Guro'
print('a =', a) # a = {'phone': '01012345678', 'birth': '010203', 'Address': 'Guro', 'Rank': [1, 2, 3], 'test': 'test_dict'}
a.update(birth = '020202')
print("a.update(birth = '020202') =", a) # a.update(birth = '020202') = {'phone': '01012345678', 'birth': '020202', 'Address': 'Guro', 'Rank': [1, 2, 3], 'test': 'test_dict'}

temp = {'Address': 'Busan'}
a.update(temp)
print("a.update(temp) =", a)