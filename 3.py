import pandas as pd
import numpy as np

df = pd.read_csv('./ex.csv', encoding = 'utf-8')
df #14026 rows x 18columns

df.info()
df.isnull().sum()

# win or lose 외에 게임 있는지 확인 ex.다시하기 - 전부 lose로 처리되어 필요가 없음
# idxw = df[df['recent_results'] == 'win'].index
# idxl = df[df['recent_results'] == 'lose'].index

# 중복 게임 제거 idx1찾기

df.columns
df['recent_time']
df['time_stamp']
df['key'] = df['recent_time'] + df['time_stamp']
df['key']

df['key'] = df['key'].drop_duplicates(keep='last')
df['key'][0]
df['key'].isnull()


idx1 = df[df['key'].isnull() == True].index
idx1 #중복 14026 - 6336= 

# 15분 미만게임 제거 idx2 찾기
df['recent_time'] = df['recent_time'].apply(lambda x : ((x).replace('분 ',':')))
df['recent_time'] = df['recent_time'].apply(lambda x : ((x).replace('초','')))
df['recent_time_min'] = df['recent_time'].apply(lambda x : int(x.split(':')[0]))
df['recent_time_min']
idx2 = df[df['recent_time_min'] < 15].index
idx2

# idx1 과 idx2 합치기 (한번에 제거해야 오류 ㄴ)
idx1 #6336
idx2 #192
type(idx1)
len(df)

idx3 = []
for i in range(len(df)):
    if i in idx1 or i in idx2:
        idx3.append(i)

#idx3

df1 = df.drop(idx3)
df1 # 7575 X 20
df1.reset_index(drop=True, inplace=True)
df1.to_csv('exex.csv', encoding = 'utf-8')
