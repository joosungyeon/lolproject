import pandas as pd
import numpy as np

df = pd.read_csv('./lol_rate.csv', encoding = 'utf-8')

df

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

# 승률 상위 5캐릭 보여주기 포지션 상관없음
df1.reset_index(drop=True, inplace=True)

print(df1['Champ'][0], df1['win_rate'][0], str(df1['total_game'][0])+'경기 사용')
print(df1['Champ'][1], df1['win_rate'][1], str(df1['total_game'][1])+'경기 사용')
print(df1['Champ'][2], df1['win_rate'][2], str(df1['total_game'][2])+'경기 사용')
print(df1['Champ'][3], df1['win_rate'][3], str(df1['total_game'][3])+'경기 사용')
print(df1['Champ'][4], df1['win_rate'][4], str(df1['total_game'][4])+'경기 사용')
#print(df1['Champ'][5], df1['win_rate'][5], str(df1['total_game'][5])+'경기 사용')




######## 100 게임 미만 챔프 삭제

# idx = df1[df1['total_game'] < 100].index
# df2 = df1
# df2 = df2.drop(idx)
# df2.reset_index(drop=True, inplace = True)
# df2
# print(df2['Champ'][0], df2['win_rate'][0])
# print(df2['Champ'][1], df2['win_rate'][1])
# print(df2['Champ'][2], df2['win_rate'][2])
# print(df2['Champ'][3], df2['win_rate'][3])
# print(df2['Champ'][4], df2['win_rate'][4])
# print(df2['Champ'][5], df2['win_rate'][5])



# 포지션에 맞는 챔피언 추천

        
# 포지션 값 받아서 지정
mypos = input('포지션 입력 (선택)')


print('나의 포지션은 ' + mypos + '입니다')

if mypos == 'top':
    df1[df1['top_pick_rate'] > 30].head()
elif mypos == 'jungle':
    df1[df1['jungle_pick_rate'] > 30].head()
elif mypos == 'mid':
    df1[df1['mid_pick_rate'] > 30].head()
elif mypos == 'adcarry':
    df1[df1['adcarry_pick_rate'] > 30].head()
elif mypos == 'support':
    df1[df1['support_pick_rate'] > 30].head()
