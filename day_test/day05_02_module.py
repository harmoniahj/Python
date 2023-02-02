# Module : 함수, 변수, 클래스 등 python 구성요소 등을 모아놓은 파일
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

# print('called! inner!')
# print('add(5,5) : {} // subtract(8,4) : {}'.format(add(5,5), subtract(8,4))) # add(5,5) : 10 // subtract(8,4) : 4
# print('multiply(5,5) : {} // divide(8,4) : {}'.format(multiply(5,5), divide(8,4))) # multiply(5,5) : 25 // divide(8,4) : 2.0

# __name__ 사용
if __name__ == "__Main__":
    print('called! inner!')
    print('add(5,5) : {} // subtract(8,4) : {}'.format(add(5,5), subtract(8,4))) # add(5,5) : 10 // subtract(8,4) : 4
    print('multiply(5,5) : {} // divide(8,4) : {}'.format(multiply(5,5), divide(8,4))) # multiply(5,5) : 25 // divide(8,4) : 2.0