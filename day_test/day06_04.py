# 파일 읽기 및 쓰기
# r : 읽기, w : 쓰기, a : 추가, t : 텍스트, b : 바이너리
# 상대경로 '../', '/', 절대경로 : 'C:\Users\Python\day_test'

# 파일 읽기
f = open('resource/it_news.txt', 'r', encoding='UTF-8')
print(dir(f))
print(f.encoding) # 인코딩 확인
print(f.name) #  파일명
print(f.mode) # 모드 확인

cts = f.read()
print(cts)

f.close() # 반드시 닫기

# with문 사용
with open('resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print('iter(c) :', iter(c))
    print('list(c) :', list(c))

# read() : 전체 일기, read(10) : 10byt만 읽기(공백포함)
with open('resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20) # Three ways networkin
    print(c)
    print('iter(c) :', iter(c)) # iter(c) : <str_ascii_iterator object at 0x00000174B651BF70>
    print('list(c) :', list(c)) # list(c) : ['T', 'h', 'r', 'e', 'e', ' ', 'w', 'a', 'y', 's', ' ', 'n', 'e', 't', 'w', 'o', 'r', 'k', 'i', 'n']

    c = f.read(20)
    print(c) # g services simplify

# readline : 한줄씩 읽기
with open('resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line) # Three ways networking services simplify network management

    line = f.readline()
    print(line) # Organizations rely on networks to power their work.

# readlines : 전체를 읽은 후 라인 단위를 리스트로 저장
with open('resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)

    for c in cts:
        print(c, end = '')
    
print('END!!')

# 파일 쓰기
with open('resource/contents.txt', 'w') as f:
    f.write('I Love Python ~!\n')

with open('resource/contents.txt', 'at') as f: # a : 추가하여 쓰기
    f.write('I Love Python ~!~!\n')

# writelines : 리스트 -> 파일로 쓰기
with open('resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

with open('resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file = f)
    print('Test Text Write2!', file = f)
    print('Test Text Write!3', file = f)