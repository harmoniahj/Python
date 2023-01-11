import sys
import inspect
# from ..sub1 import mudule1

# module2.py
def mod2_test1():
    print("Module2 -> Test1")
    # 현재 이 파일이 실행되는 inspect.getfile의 현재 경로 나타내는 메소드 호출
    print("Path :", inspect.getfile(inspect.currentframe()))

def mod2_test2():
    print("Module2 -> Test2")
    print("Path :", inspect.getfile(inspect.currentframe()))