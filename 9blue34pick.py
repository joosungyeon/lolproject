#블루 3,4픽
import pandas as pd
import numpy as np

df = pd.read_csv('./lol_rate3.csv', encoding = 'utf-8')


# 승률 순으로 정렬
df1 = df.sort_values(by='win_rate', ascending = False, axis= 0)
df1.reset_index(drop=True, inplace=True)
df1

# 밴 10캐릭 등록
ban1 = input('ban1 입력해주세요')

ban2 = input('ban2 입력해주세요')

ban3 = input('ban3 입력해주세요')

ban4 = input('ban4 입력해주세요')

ban5 = input('ban5 입력해주세요')

ban6 = input('ban6 입력해주세요')

ban7 = input('ban7 입력해주세요')

ban8 = input('ban8 입력해주세요')

ban9 = input('ban9 입력해주세요')

ban10 = input('ban10 입력해주세요')

b1pick = input('blue 1픽 입력해주세요')

r1pick = input('red 1픽 입력해주세요')

r2pick = input('red 2픽 입력해주세요')

# 밴 10캐릭 제거

idxb1 = df1[df1['Champ'] == ban1].index
idxb2 = df1[df1['Champ'] == ban2].index
idxb3 = df1[df1['Champ'] == ban3].index
idxb4 = df1[df1['Champ'] == ban4].index
idxb5 = df1[df1['Champ'] == ban5].index
idxb6 = df1[df1['Champ'] == ban6].index
idxb7 = df1[df1['Champ'] == ban7].index
idxb8 = df1[df1['Champ'] == ban8].index
idxb9 = df1[df1['Champ'] == ban9].index
idxb10 = df1[df1['Champ'] == ban10].index
idxb11 = df1[df1['Champ'] == b1pick].index
idxb12 = df1[df1['Champ'] == r1pick].index
idxb13 = df1[df1['Champ'] == r2pick].index

# idxb1
# idxb2


df1 = df1.drop(idxb1)
df1 = df1.drop(idxb2)
df1 = df1.drop(idxb3)
df1 = df1.drop(idxb4)
df1 = df1.drop(idxb5)
df1 = df1.drop(idxb6)
df1 = df1.drop(idxb7)
df1 = df1.drop(idxb8)
df1 = df1.drop(idxb9)
df1 = df1.drop(idxb10)
df1 = df1.drop(idxb11)
df1 = df1.drop(idxb12)
df1 = df1.drop(idxb13)

# 승률 상위 5캐릭 보여주기 포지션 상관없음


##################### blue1 픽과 red 1,2픽을 고려한 데이터

df1.reset_index(drop=True, inplace=True)

print(df1['Champ'][0], df1['win_rate'][0], str(df1['total_game'][0])+'경기 사용')
print(df1['Champ'][1], df1['win_rate'][1], str(df1['total_game'][1])+'경기 사용')
print(df1['Champ'][2], df1['win_rate'][2], str(df1['total_game'][2])+'경기 사용')
print(df1['Champ'][3], df1['win_rate'][3], str(df1['total_game'][3])+'경기 사용')
print(df1['Champ'][4], df1['win_rate'][4], str(df1['total_game'][4])+'경기 사용')


