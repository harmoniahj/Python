# OOP (객체지향 프로그래밍), Self, Instance, Method, 인스턴스 변수

# Class
class Dog: # Object 상속 = class Dog(object)
    # class 속성
    species = 'firstdog'

    # 초기화/Instance 속성
    def __init__(self, name, age): # 초기화를 위한 함수(메소드), 반드시 첫번째 인수는 self
        self.name = name
        self.age = age

# class 정보
# class 변수 : 직접 접근 가능, 공유
print(Dog) # <class '__main__.Dog'>

# Instance : class에 정의된 데이터 or 함수 사용하기 위해 생성, 하나의 class에 대해 여러개의 인스턴스 생성 가능
# Instance 변수 : 객체마다 별도로 존재
a = Dog("Mikky", 2)
b = Dog("Puppy", 5)

print('a == b :', a == b, 'id(a) :', id(a), 'id(b) :', id(b)) # a == b : False id(a) : 2903377261392 id(b) : 2903377261328

# namespace : 객체를 인스턴스화 할때 저장된 공간
print('dog1 a.__dict__ :', a.__dict__) # dog1 a.__dict__ : {'name': 'Mikky', 'age': 2} => Dictionary 형태로
print('dog1 b.__dict__ :', b.__dict__) # dog1 b.__dict__ : {'name': 'Puppy', 'age': 5}

# 인스턴스 속성 
print('{} is {} // {} is {}'.format(a.name, a.age, b.name, b.age)) # Mikky is 2 // Puppy is 5

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.age)) # Mikky is a 2

print(Dog.species) # firstdog
print(a.species) # firstdog
print(b.species) # firstdog

# Self : 인스턴스 자신 or 그 시점의 자신 or 메소드의 임의의 인수
class SelfTest:
    def func1():
        print('Function called')
    
    def func2(self):
        print('Function self called')
        # print('id(self) :', id(self)) # id(self) : 2360270143312

f = SelfTest()

# print('dir(f) :', dir(f))
print('id(f) :', id(f)) # id(f) : 2580625505744
# f.func1() # 에러
f.func2() # Function self called

SelfTest.func1() # Function called
SelfTest.func2(f) # Function self called

# class 변수, Instance 변수
class Warehouse:
    stock_num = 0

    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __delattr__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Kim')

print('stock_num :', Warehouse.stock_num) # stock_num : 2
print('user1.name : {} // user.name : {}'.format(user1.name, user2.name)) # user1.name : Lee // user.name : Kim
print('user1.__dict__ : {} // user2.__dict__ : {}'.format(user1.__dict__, user2.__dict__)) # user1.__dict__ : {'name': 'Lee'} // user2.__dict__ : {'name': 'Kim'}
print(Warehouse.stock_num, user1.stock_num) # 2 2

del user1
print(Warehouse.__dict__)

# ex)
class Dog1:
    species = 'firstdog'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# 인스턴스 생성
c = Dog1('July', 4)
d = Dog1('Marry', 10)

# Method : clalss 내의 개재되어 있는 함수, 여러개의 메소드 정의 가능
# Method 호출
print(c.info()) # July is 4 years old
print(c.speak('Wal! Wal!')) # July says Wal! Wal!
print(d.info()) # Marry is 10 years old
print(d.speak('Woof! Woof')) # Marry says Woof! Woof