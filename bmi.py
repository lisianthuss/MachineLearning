#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import tensorflow as tf


# 키, 몸무게, 레이블이 적인 csv 파일 읽어 들이기
csv = pd.read_csv("bmi.csv")

# 데이터 정규화
csv["height"] = csv["height"] / 200
csv["weight"] = csv["weight"] / 100

# label을 table로 변환
# - thin=(1,0,0) / normal=(0,1,0) / fat=(0,0,1)
bclass = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x: np.array(bclass[x]))

