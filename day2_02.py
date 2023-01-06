# 자료형 - 문자형
str1 = 'I am Python'
str2 = "Have a Good Day~~"
str3 = '''How are you?'''
str4 = """Thank you~!"""

# str = <class 'str'> str2 = <class 'str'> str3 = <class 'str'> str4 = <class 'str'>
print('str1 =', type(str1), 'str2 =', type(str2), 'str3 =', type(str3), 'str4 =', type(str4))
print('str1 =', str1, 'str2 =', str2, 'str3 =', str3, 'str4 =', str4) # str = I am Python str2 = Have a Good Day~~ str3 = How are you? str4 = Thank you~!

# 빈 문자열
str5 = ''
str6 = str()

print('str5 =', type(str5), 'str6 =', type(str6)) # str5 = <class 'str'> str6 = <class 'str'>
print('len(str5) =', len(str5), 'len(str6) =', len(str5)) # len(str5) = 0 len(str6) = 0

# Escape 문자
'''
 /n : 개행문자, \t : 탭
 \\ : 문자, \' : 문자
 \" : 문자, \000 : 널 문자
'''
print("I'm Python") # I'm Python : print('I'm Python') -> 에러발생
print('I\'m Python') # I'm Python
print('Hi \t Hi~') # Hi       Hi~
print('a \"\" b') # a "" b

escape_str = "Do uot have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'

print('escape_str =', escape_str) # escape_str = Do uot have a "retro games"?
print('escape_str2 =', escape_str2) # escape_str2 = What's on TV?

# 탭, 줄 바꿈
t_s1 = "Click \t Start~!"
t_s2 = "New Line \n Check!"

print('t_s1 =', t_s1, 't_s2 =', t_s2)

# Raw String
raw_s = r'C:\python\test'
print('raw_s = ', raw_s) # raw_s =  C:\python\test

# Multi Line
multi_str = \
'''
Love as powerful as your mother's for you leaves it's own mark.
To have been loved so deeply, even though the person who loved us is gone, will give us some protection forever.
'''
print('multi_str =', multi_str)

# 문자열 연산
str_01 = "Python"
str_02 = "Test"
str_03 = "How are you doing"
str_04 = "Study"

print('str_01 * 3 =', str_01 * 3) # str_01 * 3 = PythonPythonPython
print('str_01 + str_02 =', str_01 + str_02) # str_01 + str_02 = PythonTest
print("'y' in str_01 =", 'y' in str_01) # 'y' in str_01 = True -> y가 없으면 False 반환
print("'P' not in str_01 =", 'P' not in str_02) # 'P' not in str_01 = True

# 문자열 형 변환
print('str(66) =', str(66), 'type(str(66))', type(str(66))) # str(66) = 66 type(str(66)) <class 'str'>

# 문자열 함수 : upper, isalnum, startswith, count, endswith, isalpha ...
str_01 = "python"
print("str_01.capitalize =", str_01.capitalize()) # str_01.capitalize = Python : 첫번째 시작 글자 대문자로 변화
print("str_01.endswith =", str_01.endswith("n")) # str_01.endswith = True : 마지막 문자 체크
print("str_01.replace =", str_01.replace("python", "Good")) # str_01.replace = Good
print('sorted(str_01) =', sorted(str_01)) # sorted(str_01) = ['h', 'n', 'o', 'p', 't', 'y']
print('str_03.split =', str_03.split(' ')) # str_03.split = ['How', 'are', 'you', 'doing'] : 공백을 기준으로 분리

# 반복(Sequence)
im_str = "Good Day!"
print('dir(im_str) =', dir(im_str)) # __iter__ : Sequence 반복 가능
for i in im_str:
    print('i =', i)

# 슬라이싱
str_sl = "Nice Python"
print('len(str_sl', len(str_sl), 'str_sl =', str_sl[0:3]) # len(str_sl 11 str_sl = Nic : 0~2 까지의 문자 출력
print(str_sl[5:11]) # Python = print(str_sl[5:])
print('str_sl[:] =', str_sl[:], 'str_sl[:len(str_sl)] =', str_sl[:len(str_sl)]) # str_sl[:] = Nice Python str_sl[:len(str_sl)] = Nice Python
print('str_sl[1:4:2] =', str_sl[1:9:2]) # str_sl[1:4:2] = iePt
print('str_sl[-5:] =', str_sl[-5:]) # str_sl[-5:] = ython
print('str_sl[1:-2] =', str_sl[1:-2]) # str_sl[1:-2] = ice Pyth : 끝에서 -1
print('str_sl[::2] =', str_sl[::2]) # str_sl[::2] = Nc yhn
print('str_sl[::-1] =', str_sl[::-1]) # str_sl[::-1] = nohtyP eciN

# 아스키코드 or 유니코드
a = 'z'
print('ord(a) =', ord(a)) # ord(a) = 122 : 아스키코드로 출력
print('chr(122 =', chr(122)) # chr(122 = z : 문자로 출력