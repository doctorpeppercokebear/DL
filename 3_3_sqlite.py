import sqlite3
import pandas as pd
import numpy

# CRUD : Creat, Read, Update, Delete

# 퀴즈 1
# kma.csv 파일을 2차원 리스트로 반환하는 함수를 만드세요
# kma = pd.read_csv('kma.csv')
# print(kma)

def read_kma():
    with open('kma.csv', 'r', encoding='utf-8') as f:
        return [line.strip().split(',') for line in f]

def create_db():
    conn = sqlite3.connect('data/kma.sqllite3')
    cursor = conn.cursor()      #

    query = 'CREATE TABLE kma (prov TEXT, city TEXT, mode TEXT, tmEf TEXT, wf TEXT, tmn TEXT, tmx TEXT, rnSt TEXT)'
    cursor.execute(query)

    conn.commit()
    conn.close()

create_db()

rows = read_kma()
# print(*rows, sep='\n')


def insert_row(row):
    conn = sqlite3.connect('data/kma.sqllite3')
    cursor = conn.cursor()      #

    # 퀴즈
    # row에 들어있는 데이터를 전달하세요.
    base = 'INSERT INTO kma (prov) VALUES({},{},{},{},{},{},{},{},)'
    query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    cursor.execute(query)

    conn.commit()
    conn.close()

    create_db()

# 퀴즈 insert_all 함수를 만드세요
def insert_all(rows):
    conn = sqlite3.connect(('data/kma.sqlite3'))
    cursor = conn.cursor()

    base = 'INSERT INTO kma (prov) VALUES({},{},{},{},{},{},{},{},)'
    for row in rows:
        query = base.format(*row)
        cursor.execute(query)

    conn.commit()
    conn.close()



def fetch_all(row):
    conn = sqlite3.connect('data/kma.sqllite3')
    cursor = conn.cursor()  #

            # 퀴즈
            # row에 들어있는 데이터를 전달하세요.
    base = 'INSERT INTO kma (prov) VALUES({},{},{},{},{},{},{},{},)'
    query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], )
    cursor.execute(query)

    conn.commit()
    conn.close()



rows = fetch_all()

print(*rows, sep='\n')
