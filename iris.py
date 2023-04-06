#基本ライブラリ
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

#データセット読み込み
iris=load_iris()
df=pd.DataFrames(iris.data,columns=iris.feature_names)

#目標値
df['target']=iris.target

#目標値を数字から花の名前に変更
df.loc[df['target']]==0,'target']='setosa'
df.loc[df['target']]==1,'target']='varsicolor'
df.loc[df['target']]==2,'target']='virginica'

