import time
import random
import os
from tutorial import tutorial
from game import run

def game_start():
    os.system('cls')
    print("""
          
            =====================================================
                                            
                #    #   ##   #    # ###### 
                ##  ##  #  #  #   #  #      
                # ## # #    # ####   #####  
                #    # ###### #  #   #      
                #    # #    # #   #  #      
                #    # #    # #    # ###### 
            =====================================================
                                                #####  
                 ####    ##   #    # ######    #     # 
                #    #  #  #  ##  ## #               # 
                #      #    # # ## # #####         #  
                #  ### ###### #    # #           #     
                #    # #    # #    # #         #      
                 ####  #    # #    # ######   ########     
            =====================================================                                                                 
    """)
    time.sleep(2)
    os.system("cls")
    print("make_game_2 에 오신 것을 환영합니다.")
    while(1):
        print("원하는 메뉴의 번호를 입력한 다음 Enter키를 누르세요.")
        print("1.게임시작")
        print("2.게임설명")
        print("3.게임종료")
        command = input(">>")
        os.system("cls")
        if command =='1':
            run()
        elif command =='2':
            tutorial()
        elif command == '3':
            print("이용해주셔서 감사합니다.")
            time.sleep(1.5)
            break
        else:
            print("잘못 누르셨습니다.")
            print()

if __name__ == "__main__":
    game_start()