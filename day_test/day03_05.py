# if문
print('type(True) =', type(True)) # 0이 아닌 수 , "abc", [1, 2, 3], (1, 2, 3) ...
print('type(False) =', type(False)) # 0, "", [], {}, ()

if True:
    print('Good~!')

if False:
    print('Bad')

if False:
    print('Bad')
else:
    print('Good~!')

# 관계연산자 : >, >=, <, <=, ==, !=
x = 15
y = 10

print('x > y :', x > y) # x > y : True
print('x >= y :', x >= y) # x >= y : True
print('x < y :', x < y) # x < y : False
print('x <= y :', x <= y) # x <= y : False
print('x == y :', x == y) # x == y : False
print('x != y :', x != y) # x != y : True

city = ""

# Please enter your city 출력
if city:
    print("You are in", city)
else:
    print("Please enter your city")

city2 = "Seoul"

if city2:
    print("You are in", city2)
else:
    print("Please enter your city")

# 논리 연산자 : and, or, not
a = 75
b = 40
c = 10

print('a > b and b > c :', a > b and b > c) # a > b and b > c : True
print('a > b or b > c :', a > b or b > c) # a > b or b > c : True
print('not a > b :', not a > b) # not a > b : False
print('not True :', not True) # not True : False
print('not False :', not False) # not False : True

# 산술, 관계, 논리 우선순위 (산술 > 관계 > 논리)
print('ex)', 3+12 > 7+3) # ex) True
print('ex)', 5 + 20 * 3 > 7 + 3 * 20) # ex) False
print('ex)', 5 + 10 * 3 > 7 and 7 + 3 == 10) # ex) True

score = 90
score2 = 'A'

if score >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

id = 'vip'
id2 = 'admin'
grade = 'Platinum'

if id == 'vip' or id2 == 'admin':
    print("관리자 입장")
if id2 == 'admin' and grade == 'Platinum':
    print("촤상위 관리자")

# 다중 조건문
num = 65

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('Grade : F')

# 중첩 조건문
grade = 'A'
total = 60

if grade == 'A':
    if total >= 90:
        print('장학급 100%')
    elif total >= 80:
        print('장학급 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')

# in, not in
q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {'name': "Lee", 'city':'Seoul', 'grade': 'A'}
r = (1, 2, 3)

print('20 in q :', 20 in q) # 20 in q : True
print('12 not in r :', 12 not in r) # 12 not in r : True
print("'Seoul' in e.values() :", 'Seoul' in e.values())