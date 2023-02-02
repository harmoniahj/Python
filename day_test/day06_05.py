# CSV파일 읽기 및 쓰기
import csv

with open('resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 헤더 생략

    print(reader) # 객체 확인
    print(type(reader)) # 타입확인
    print(dir(reader)) # 속성확인 __iter__ : 있으면 for문 가능

    for c in reader:
        # print(c)
        # list to str
        print(':'.join(c)) # MM:MYANMAR ...

with open('resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')

    for c in reader:
        print(c)

with open('resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)

    print(reader)
    print(type(reader))
    print(dir(reader))
    
    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('=======================')

# 쓰기
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]

with open('resource/write1.csv', 'w', encoding='UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    print(dir(wt))

    for v in w:
        wt.writerow(v)

with open('resource/write2.csv', 'w', encoding='UTF-8') as f:
    #  필드명
    fields = ['One', 'Two', 'Three']

    # Dict Writer
    wt = csv.DictWriter(f, fieldnames=fields)

    # Header Writer
    wt.writeheader()

    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})