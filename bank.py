import pandas as pd
import os

def Int_Test():
    while True:
        try:
            value = int(input("금액 : "))  # 바로 int()로 변환
            return value                   # 변환 성공하면 반환
        except ValueError:
            print("잘못된 입력입니다. 숫자를 다시 입력해주세요.")

def bank_go():
    base_dir = os.path.dirname(__file__)
    player_csv_path = os.path.join(base_dir, "data", "player.csv")
    players = pd.read_csv(player_csv_path, encoding="utf-8")

    player_now = players[ players['ID'] == 'player_now' ]
    money = player_now["money"].iloc[0]
    bank_checking_account = player_now["bank_checking_account"].iloc[0]

    exit_bank = False
    while exit_bank == False:
        print("\n\n영란 은행")
        print(f"지갑 : {money} / 계좌 : {bank_checking_account}")
        action = input("1) 나가기 / 2) 계좌에 돈널기 / 3) 계좌에서 돈 꺼내기\n행동 : ").replace(" ", "")
        if action == "1":
            exit_bank = True
            continue
        elif action == "2":
            print(f"지갑 : {money} / 계좌 : {bank_checking_account}\n입금")
            deposit = Int_Test()
            if deposit > money:
                os.system("cls")
                print("현금이 부족합니다.")
            else:
                bank_checking_account += deposit
                money -= deposit
                os.system("cls")
        elif action == "3":
            print(f"지갑 : {money} / 계좌 : {bank_checking_account}\n출금")
            Withdrawal = Int_Test()
            if Withdrawal > bank_checking_account:
                os.system("cls")
                print("잔액이 부족합니다.")
            else:
                bank_checking_account -= Withdrawal
                money += Withdrawal
                os.system("cls")

        else:
            os.system("cls")
            print("1, 2, 3 중 입력하십시오.")
            
    # player["money"].iloc[0] = money
    # player["bank_checking_account"].iloc[0] = bank_checking_account
    # 변수만 바뀌고 csv 는 그대로
    players.loc[players["ID"] == "player_now", "money"] = money
    players.loc[players["ID"] == "player_now", "bank_checking_account"] = bank_checking_account
    players.to_csv(player_csv_path, index=False, encoding="utf-8")
    
if __name__ == "__main__":
    bank_go()