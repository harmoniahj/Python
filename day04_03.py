# Function
# 함수 정의 방법
# def function_name(parameter):
#   code

def first_func(w):
    print("Hello,", w)

word = "Nice Day~!"

first_func(word)

def return_func(w):
    value = "Hello, " + str(w)
    return value

x = return_func('Have a Nice Day')
print(x) # Hello, Have a Nice Day

# 다중 반환
def fun_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = fun_mul(10)

print('x =', x, 'y =', y, 'z =', z) # x = 100 y = 200 z = 300

# Tuple return
def fun_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = fun_mul2(20)
print('type(q) :',type(q),'q :', q) # type(q) : <class 'tuple'> q : (200, 400, 600)

# List return
def fun_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = fun_mul3(30)
print('type(p) :',type(p),'set(p) :', set(p)) # type(p) : <class 'list'> set(p) : {200, 600, 400}

# Dictionary return
def fun_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1':y1, 'v2':y2, 'v3':y3}

d = fun_mul4(40)
print('type(d) :',type(d),"d.get('v2') :", d.get('v2')) # type(d) : <class 'dict'> d.get('v2') : 800

# *args (unpacking) : 튜플형태로 보낼때
def args_func(*args): # 매개변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('------')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# **kwargs (unpacking)
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('======')

kwargs_func(name1 = ': Lee')
kwargs_func(name1 = ': Lee', name2 = ': Park')
kwargs_func(name1 = ': Lee', name2 = ': Park', name3 = ': Kim')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print('args_1 :', args_1, 'args_2 :', args_2, 'args :', args, 'kwargs :', kwargs)
    # args_1 : 10 args_2 : 20 args : ('Lee', 'Park', 'Kim') kwargs : {'age1': 20, 'age2': 30, 'afe3': 40}

example(10, 20, 'Lee', 'Park', 'Kim', age1=20, age2=30, afe3=40)

# 중첩 함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)
# func_in_func(1000) > 사용불가

# 람다식 : 메모리 절약 + 가독성 향상 + 코드 간결 => 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# => 남발시 가독성 오히려 감소
# 함수 : 객체 생성 -> 리소스(메모리) 할당

# 일반적함수 -> 할당
def mul_func(x, y):
    return x * y

# q = mul_func(10, 50)
# print('q :', q)
print('mul_func(10, 50) :', mul_func(10, 50)) # mul_func(10, 50) : 500

mul_func_var = mul_func
print('mul_func_var(20, 50) :', mul_func_var(20, 50)) # mul_func_var(20, 50) : 1000

# lambda 함수 -> 할당
lambda_mul_func = lambda x, y:x*y
print('lambda_mul_func(50, 50) :', lambda_mul_func(50, 50)) # lambda_mul_func(50, 50) : 2500

def func_final(x, y, func):
    print('func_final() :', x * y * func(10, 10))

func_final(10, 20, lambda x, y:x*y) # func_final() : 20000
func_final(10, 20, lambda_mul_func) # func_final() : 20000