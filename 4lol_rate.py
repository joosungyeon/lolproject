import pandas as pd
import numpy as np

df = pd.read_csv('./exex.csv', encoding = 'utf-8')
df.info() #7575 game
df.columns

Champion_list = []
for i in range(1,11):
    a = 'Champion' + str(i)
    for Champ in df[a].unique():
        if Champ not in Champion_list:
            Champion_list.append(Champ)
        else:
            pass
    
print(Champion_list)
len(Champion_list) #157
# 22/1/7일기준 157개 챔프

with open('lol_rate.csv', 'w', encoding = 'utf-8') as file:
    file.write('{},{},{},{},{},{},{},{},{},{}\n'.format('Champ','total_game','win_game','lose_game','win_rate','top_pick_rate', 'jungle_pick_rate', 'mid_pick_rate', 'adcarry_pick_rate', 'support_pick_rate'))
    
    
for Champ in Champion_list:
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
        b = df[a].str.count(Champ).sum()
        total_game += b
        if 0 < i < 6:
            win_game += b   
        elif 5 < i < 11:
            lose_game += b    
    
    for i in range(1,11):
        a = 'Champion' + str(i)
        b = df[a].str.count(Champ).sum()    
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
    with open('lol_rate.csv', 'a', encoding = 'utf-8') as file:
        file.write("{},{},{},{},{:0.2f},{:0.2f},{:0.2f},{:0.2f},{:0.2f},{:0.2f}\n".format(Champ, total_game, win_game, lose_game, win_rate, top_pick_rate, jungle_pick_rate, mid_pick_rate, adcarry_pick_rate, support_pick_rate))

