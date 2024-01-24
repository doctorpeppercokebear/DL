# 2차원 리스트
import csv
# def read_us500():
#     f = open('data/us-500.csv', 'r', encoding='uft-8')
#
#     rows = []
#     # for i, line in f:          # 모든 라인 읽는다.
#     #
#     #     # print(line.strip().split(','))
#     #     rows.append(eval(line.strip()))
#
#     f.readline()
#     for line in f:
#         rows.append((list(eval(line.strip()))))
#
#     f.close()
#     return rows
#
# rows = read_us500()
# print(*rows[:3], sep='\n')

def read_us500_2():
    f = open('data/us-500.csv', 'r', encoding='utf-8')

    rows = []

    f.readline()
    for items in csv.reader(f):
        rows.append(items)
        print(items)

    f.close()
    return rows

rows = read_us500_2()
print(*rows[:3], sep='\n')


#  작성할 때는 csv.writer()