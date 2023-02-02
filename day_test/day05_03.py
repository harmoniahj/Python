# Package
# 상대경로 : .. : 부모 디렉토리, . : 현재 디렉토리 -> Module 네부에서만 사용

# ex)
import day05_03_package.sub1.module1
import day05_03_package.sub2.module2

print("\n예제 1)")
day05_03_package.sub1.module1.mod1_test1()
day05_03_package.sub1.module1.mod1_test2()
day05_03_package.sub2.module2.mod2_test1()
day05_03_package.sub2.module2.mod2_test2()

# ex2)
from day05_03_package.sub1 import module1
from day05_03_package.sub2 import module2 as m2

print("\n예제 2)")

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

# ex3)
from day05_03_package.sub1 import *
from day05_03_package.sub2 import *

print("\n예제 3)")
module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()