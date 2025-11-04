import pandas as pd
import numpy as np
import math
import os

def run():
    base_dir = os.path.dirname(__file__)
    player_csv_path = os.path.join(base_dir, "data", "player.csv")
    players = pd.read_csv(player_csv_path, encoding="utf-8")
    available_players = players[~players["ID"].isin(["player_now", "player_new"])]

    exit = True
    while exit:
        action = input("1) 새 게임 시작 / 2) 이어하기\n 선택 : ").replace(" ", "")
        os.system("cls")
        if action == "1":
            print(f'세이브 목록\n{available_players["name"]}')
            new_player_name = input("새 플레이어 이름\n(공백 시 되돌아감): ").strip().replace(" ", "_")
            duplication_test_player = players[players['ID'] == f"player_{new_player_name}"]
            if new_player_name == "":
                os.system("cls")
                continue
            elif duplication_test_player.empty:
                pass
            else:
                print(f"이미 {new_player_name}라는 플레이어가 있습니다.")
                continue
            new_player = players[players['ID'] == "player_new"]
            new_player.loc[:, "ID"] = f"player_{new_player_name}"
            new_player.loc[:, "name"] = f"{new_player_name}"
            players = pd.concat([players, new_player], ignore_index=True)
            
            now_player_id = f"player_{new_player_name}"
            now_player = players[players['ID'] == now_player_id]
            exit = False
            
        elif action == "2":
            print(f'세이브 목록\n{available_players["name"]}')
            #load
            load_player_name = input("시작할 플레이어 선택\n(공백 시 되돌아감): ")
            if load_player_name == "":
                os.system("cls")
                continue
            
            now_player_id = f"player_{load_player_name}"
            now_player = players[players['ID'] == now_player_id]
            if now_player.empty:
                print("해당 이름을 가진 플레이어가 없습니다.")
                continue
            exit = False
            
        else:
            print("1, 2 중 입력하십시오.")

    start_idx = players.columns.get_loc("start") + 1
    end_idx = players.columns.get_loc("end")
    update_columns = players.columns[start_idx:end_idx].tolist()
    for col in update_columns:
        players.loc[players["ID"] == "player_now", col] = now_player[col].values[0]           
    players.to_csv(player_csv_path, index=False, encoding="utf-8-sig")
    
    return players[players["ID"] == "player_now",]

if __name__ == "__main__":
    run()