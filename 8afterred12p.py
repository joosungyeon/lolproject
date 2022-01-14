import pandas as pd
import numpy as np

df = pd.read_csv('./exex.csv', encoding = 'utf-8')
df


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


ban_list = [ban1, ban2, ban3, ban4, ban5, ban6, ban7, ban8, ban9, ban10]
ban_list
df1 = df

for ban_champ in ban_list:
    idxban = df1[(df1['Champion1']==ban_champ) | (df1['Champion2']==ban_champ) | (df1['Champion3']==ban_champ) | (df1['Champion4']==ban_champ) | (df1['Champion5']==ban_champ) | (df1['Champion6']==ban_champ) | (df1['Champion7']==ban_champ) | (df1['Champion8']==ban_champ) | (df1['Champion9']==ban_champ) | (df1['Champion10']==ban_champ)].index
    df1 = df1.drop(idxban)
    df1.reset_index(drop=True, inplace=True)

df_ban = df1
df_ban

##### 
b1pick = input('블루 1픽')

r1pick = input('레드 1픽')

r2pick = input('레드 2픽')


df2 = df_ban[(df_ban['Champion1']==b1pick) | (df_ban['Champion2']==b1pick) | (df_ban['Champion3']==b1pick) | (df_ban['Champion4']==b1pick) | (df_ban['Champion5']==b1pick)]
df2.reset_index(drop=True, inplace=True)
df2


df3 = df2[(df2['Champion6'] == r1pick or r2pick) | (df2['Champion7'] == r1pick or r2pick) | (df2['Champion8'] == r1pick or r2pick) | (df2['Champion9'] == r1pick or r2pick) | (df2['Champion10'] == r1pick or r2pick)]
df3.reset_index(drop=True, inplace=True)
df3


Champion_list3 = []
for i in range(1,11):
    a = 'Champion' + str(i)
    for Champ in df3[a].unique():
        if Champ not in Champion_list3:
            Champion_list3.append(Champ)
        else:
            pass
    
print(Champion_list3)
len(Champion_list3) #134
# 22/1/7일기준 157개 챔프 

with open('lol_rate3.csv', 'w', encoding = 'utf-8') as file:
    file.write('{},{},{},{},{},{},{},{},{},{}\n'.format('Champ','total_game','win_game','lose_game','win_rate','top_pick_rate', 'jungle_pick_rate', 'mid_pick_rate', 'adcarry_pick_rate', 'support_pick_rate'))
    
    
for Champ in Champion_list3:
    total_game = 0
    win_game = 0
    lose_game = 0
    top_game = 0
    jungle_game = 0
    mid_game = 0
    adcarry_game = 0
    support_game = 0
    for i in range(1,11):
        a = 'Champion' + str(i)
        b = df3[a].str.count(Champ).sum()
        total_game += b
        if 0 < i < 6:
            win_game += b   
        elif 5 < i < 11:
            lose_game += b    
    
    for i in range(1,11):
        a = 'Champion' + str(i)
        b = df3[a].str.count(Champ).sum()    
        if i % 5 == 1:
            top_game += b
        elif i % 5 == 2:
            jungle_game += b
        elif i % 5 == 3:
            mid_game += b
        elif i % 5 == 4:
            adcarry_game += b
        elif i % 5 == 0:
            support_game += b
        else:
            pass
    win_rate = win_game / total_game * 100
    top_pick_rate = top_game / total_game * 100
    jungle_pick_rate = jungle_game / total_game * 100
    mid_pick_rate = mid_game / total_game * 100
    adcarry_pick_rate = adcarry_game / total_game * 100
    support_pick_rate = support_game /total_game * 100
    #print('{},{},{},{},{:0.2f}%'.format(Champ, total_game, win_game, lose_game, win_rate))
    with open('lol_rate3.csv', 'a', encoding = 'utf-8') as file:
        file.write("{},{},{},{},{:0.2f},{:0.2f},{:0.2f},{:0.2f},{:0.2f},{:0.2f}\n".format(Champ, total_game, win_game, lose_game, win_rate, top_pick_rate, jungle_pick_rate, mid_pick_rate, adcarry_pick_rate, support_pick_rate))
