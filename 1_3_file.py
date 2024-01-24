poem = open('data/poem.txt', 'r', encoding='utf-8')

# fomat, split, join 기억할 것

words = 0
for line in poem:
    print(line.strip().split())
    words += len(line.strip().split())   #split 개행 문자 제거

poem.close()

print('단어 : {}'.format(words))