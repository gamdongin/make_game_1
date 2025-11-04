import pandas as pd
import numpy as np
import math
import os

# 달걀의 경우 생산량을 더하다가 1을 넘으면 정수 자리에 있는걸 반영하는 식으로 함
# 양모는 1년에 1번 지정한 날에 처리
# 밀을 포함한 작물은 그 생장 주기에 맞춰 수확
# 우유는 매일 착유하되 건유기인 겨울은 생산 안 함

base_dir = os.path.dirname(__file__)
player_csv_path = os.path.join(base_dir, "data", "player.csv")
players = pd.read_csv(player_csv_path, encoding="utf-8")
data_prodution_csv_path = os.path.join(base_dir, "data", "data_prodution.csv")
data_prodution = pd.read_csv(data_prodution_csv_path, encoding="utf-8")
#years_circle_csv_path = os.path.join(base_dir, "data_prodution", "years_circle.csv")
#years_circle = pd.read_csv(years_circle_csv_path, encoding="utf-8")

player_now = players[ players['ID'] == "player_now" ]
# 반드시 '' 가 아닌 "" 쓸 것
# player_now = players[ players['ID'] == 'player_now' ] 에러남
player_now_series = player_now.iloc[0]

bank_checking_account = player_now_series["bank_checking_account"]
bank_interest = 0.01
bank_checking_account = float(math.trunc(bank_checking_account*((1+bank_interest)*100)/100))  # return
players.loc[ players['ID'] == "player_now","bank_checking_account"] = bank_checking_account     

days = player_now_series ["days"] + 1
players.loc[ players['ID'] == "player_now","days"] = days            # return                                                              # return

sesion = days%365
if sesion <=92:
    sesion = "spring"
elif sesion <=186:
    sesion = "summer"
elif sesion <=275:
    sesion = "fall"
else:
    sesion = "winter"

player_now_series_groth_index = player_now_series.index[player_now_series.index.str.contains('groth')]
for groth_colum in player_now_series_groth_index:
    item_groth_now = player_now_series[groth_colum]
    item_name = groth_colum[6:]
    item_row = data_prodution[data_prodution["products"].str.strip() == item_name].iloc[0]
        # 어제와 계절을 비교하여 같다면 미리 저장된 값을 쓰게 개발 예정
    item_day_yield = item_row[f"{sesion}_day_yield"]
    # 이렇게 안 하면 소숫점 자리 개판남
    item_groth_now = (item_groth_now*1000 + item_day_yield*1000)/1000
    players.loc[ players['ID'] == "player_now",players.columns.str.contains(f"groth_{item_name}")] = item_groth_now
    # return
            
players.loc[ players['ID'] == "player_now","sesion_yesterday"] = sesion # return

players.to_csv(player_csv_path, index=False, encoding="utf-8")