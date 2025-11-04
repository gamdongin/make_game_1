import pandas as pd
import numpy as np
import math
import os

script = [
    ""
]

def forest_go(player):
    while True:
        base_dir = os.path.dirname(__file__)
        player_csv_path = os.path.join(base_dir, "data", "player.csv")
        players = pd.read_csv(player_csv_path, encoding="utf-8")
            
        stamina = player["stamina"]
        
        action = input("1) 나가기 2) 숲 속 돌아다니기")
        if action == "1":
            break
        elif action == "2":
            if stamina <= 0:
                print("오늘은 너무 지쳤다.\n")
                continue
            stamina -= 1
        else:
            print("1, 2 중 입력하십시오.")
        
if __name__ == "__main__":
    forest_go()