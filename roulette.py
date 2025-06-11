playing = True
import random
import time
import sys
with open("bank.txt", "r") as balance_file:
    bank = int(balance_file.read())
def print_slow(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(0.05)  
def print_random(final_number, duration=2.5):
    start_time = time.time()
    delay = 0.01  
    while True:
        if time.time() - start_time > duration:
            break
        current_number = random.randint(0, 36)
        sys.stdout.write(f"\rRolling... {current_number} ")
        sys.stdout.flush()
        time.sleep(delay)
        delay += 0.005
while playing == True:
    if bank==0:
        print_slow("Tài khoản đã hết tiền vui lòng nạp\n")
        break
    balance_print = ("bạn có", "  ", str(bank), " VNĐ \n")
    print_slow(balance_print)
    print_slow("[1] Đỏ \n[2] Đen \n[3]số(1 ăn 35) \n[4] Thoát \n")
    a=int(input())
    
    if a == 1 or a == 2 or a == 3:
        print_slow("Nhập tiền cược: ")
        bet = int(input())
        if bet > bank:
            print_slow("Tài khoản đã hết tiền vui lòng nạp\n")
            continue
        if bet <= 0:
            print_slow("Tiền cược không hợp lệ.\n")
            continue
        if a==1 or a==2:
            print_slow("Đang quay bi ...\n")
            time.sleep(2)
            p=random.randint(1, 36)
            print_random(p)
            if p == 0:
                print_slow("Bạn thua!\n")
                bank -= bet
            else:
                if a == 1 or a == 2:
                    if p % 2 == 0:
                        if a == 2:
                            print_slow("Bạn thắng!\n")
                            bank += bet
                        else:
                            print_slow("Bạn thua!\n")
                            bank -= bet       
                    elif p % 2 == 1:
                        if a == 1:
                            print_slow("Bạn thắng!\n")
                            bank += bet
                        else:
                            print_slow("Bạn thua!\n")
                            bank -= bet
        if a==3:
            c=int(input("Nhập số bạn muốn cược: (0-36) "))
            print_slow("Đang quay bi ...\n")
            time.sleep(2)
            p=random.randint(1, 36)
            print_random(p)
            if c == p:
                print_slow("Bạn thắng!\n")
                bank += bet * 35
            else:
                print_slow("Bạn thua!\n")
                bank -= bet
        with open("bank.txt", "w") as balance_file:
            balance_file.write(str(bank))
    elif a == 4:
        print("Thoát game.")
        playing = False

