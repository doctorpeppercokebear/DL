
# 퀴즈
# iris 파일에 대해서 sparse 버전의 모델을 구축하세요
import pandas as pd
import tensorflow.keras as keras

def read_iris():
    iris = pd.read_csv('data/iris_onhot.csv')
    print(iris)



read_iris()