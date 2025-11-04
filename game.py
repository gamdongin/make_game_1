from start import start
from market import market_go
from bank import bank_go
from forest import forest_go
import os

def run():
    player = start()
    while True:
        where_go = input("목적지 선택\n 1) 시장 2) 은행 3) 인력사무소 4) 숲").replace(" ", "")
        
        if where_go == "1":
            market_go()
            os.system("cls")
        elif where_go == "2":
            bank_go()
            os.system("cls")
        elif where_go == "3":
            pass
        elif where_go == "4":
            if player["stamina"] == 0:
                print("오늘은 너무 지쳤다.")
                continue
            forest_go(player)
        else:
            print("1, 2, 3, 4 중 입력하십시오.")
            
if __name__ == "__main__":
    run()