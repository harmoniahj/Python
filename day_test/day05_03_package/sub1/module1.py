import sys
import inspect
# from ..sub2 import mudule2

# module1.py
def mod1_test1():
    print("Module1 -> Test1")
    # 현재 이 파일이 실행되는 inspect.getfile의 현재 경로 나타내는 메소드 호출
    print("Path :", inspect.getfile(inspect.currentframe()))

def mod1_test2():
    print("Module1 -> Test2")
    print("Path :", inspect.getfile(inspect.currentframe()))