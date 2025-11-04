import pandas as pd
import numpy as np
import math
import os

def Int_Action():
    while True:
        try:
            value = int(input("1) 나가기 / 2) 구매 / 3) 판매\n 선택 : "))
            return value
        except ValueError:
            print("잘못된 입력입니다. 숫자를 다시 입력해주세요.")


def market_go():
    base_dir = os.path.dirname(__file__)
    player_csv_path = os.path.join(base_dir, "data", "player.csv")
    players = pd.read_csv(player_csv_path, encoding="utf-8")
    data_prodution_csv_path = os.path.join(base_dir, "data", "data_prodution.csv")
    data_prodution = pd.read_csv(data_prodution_csv_path, encoding="utf-8")
        
    player_now = players[ players['ID'] == "player_now"]
    money = player_now["money"].iloc[0]

    # field,chicken,sheep,cow
    start_idx = players.columns.get_loc("field")
    end_idx = players.columns.get_loc("cow") + 1
    prodution_columns = players.columns[start_idx:end_idx].tolist()
    prodution_amount = player_now[prodution_columns].iloc[0]

    # name,unit,price,products,products_price,products_unit
    start_idx = data_prodution.columns.get_loc("name")
    end_idx = data_prodution.columns.get_loc("products_unit") + 1
    items_columns = data_prodution.columns[start_idx:end_idx].tolist()
    items_list = data_prodution.loc[:,items_columns]

    exit = True
    while exit:
        print(f"\nyour money : {money}\n")
        print(f"your items\n{prodution_amount}\n")    
        print(f"item list\n{items_list[["name","price"]]}\n")

        action = input("1) 나가기 / 2) 구매 / 3) 판매\n 선택 : ").replace(" ", "")
        if action == "1":
            exit = False
        elif action == "2":
            input("0) field / 1) chicken / 2) sheep / 3) cow\n 선택 : ")
        elif action == "3":
            input("0) field / 1) chicken / 2) sheep / 3) cow\n 선택 : ")
        else:
            os.system("cls")
            print("1, 2, 3 중 입력하십시오.")
            
if __name__ == "__main__":
    market_go()