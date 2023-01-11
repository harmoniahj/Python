# Module 사용
import sys

print(sys.path)
print(type(sys.path)) # <class 'list'>

# Module 경로 삽입
sys.path.append('C:\Test')
print(sys.path)

import day05_02_module

# Module 사용
print(day05_02_module.power(10, 3))