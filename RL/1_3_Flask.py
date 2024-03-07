import keras.models
import numpy as np
from flask import Flask, render_template, request
import random

# static, templates  폴더 2개를 만든다.

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, flask'


'''
퀴즈
로또 숫자 6개를 반환하는 함수를 만드세요
'''
# lotto = []
# def lotto645():
#     for i in range(1, 6):
#         lotto = random.randrange(45)
#         print(list[lotto])
#
# lotto645()

'''
강사님 코드
'''

@app.route('/lotto')            # http://127.0.0.1:5000/lotto 주소 뒤에 함수를 작성하면 된다.
def lotto645():
    a = list(range(1, 46))
    random.shuffle(a)
    return str(a[:6])


@app.route('/first')        # 127
def first():
    lotto = lotto645()
    return render_template('first.html', lotto=lotto)

@app.route('/whoru')
def show_me():
    name = request.args.get('name')
    age = request.args.get('age')

    return render_template('who-r-u.html', name=name, age=age)

'''
퀴즈
iris 모델을 구축해서
크롬 으로부터 넘겨받은 vlcj에 대해 결과를 알려 주세요
'''

app = Flask(__name__)
model = keras.models.load_model('model/iris.keras')

classes = ['setosa', 'versicolor', 'virginica']

@app.route('/iris')
def predict():
    s_len = float(request.args.get('s_len'))
    s_wid = float(request.args.get('s_wid'))
    p_len = float(request.args.get('p_len'))
    p_wid = float(request.args.get('p_wid'))

    p = model.predict([[s_len, s_wid, p_len, p_wid]], verbose=0)
    p_arg = np.argmax(p, axis=1)
    return render_template('iris.html', result=classes)

if __name__ == '__main__':
    app.run(debug=True)