# 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n)) # <class 'int'> : 타입 정수

# 동시 선언
x = y = z = 700
print(x, y, z) # 700 700 700

var = 75
# 재선언
var = "Change Value"

print(var) # Change Value
print(type(var)) # <class 'str'>

# Object References
# 변수 값 할당 상태
# 1. 타입에맞는 Object 생성 -> 2. 값 생성 -> 3. 콘솔출력
# Ex 1) 
print(300) # 300
print(int(300)) # 300

# Ex 2) n -> 777
n = 777
print(n, type(n)) # 777 <class 'int'>

m = n # m = 777 = n
print(m, type(m)) # 777 <class 'int'>

m = 400
print(m, n) # 400 777

# id(Identity) 확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m)) # 2152429109136
print(id(n)) # 2152431648816
print(id(m) == id(n)) # False

m = 800
n = 800

print(id(m)) # 2023103512464
print(id(n)) # 2023103512464
print(id(m) == id(n)) # True

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Nethod
# Pascak Case : NumberOfCollegeGraduates -> Clase
# Snake Case : number_of_college_graduates

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age = 7
_AGE_ = 8

print(age, Age, aGe, AGE, a_g_e, _age, age, _AGE_) # 7 2 3 4 5 6 7 8

# 예약어는 변수명으로 선언 불가능!