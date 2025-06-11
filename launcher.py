import subprocess
import sys
import time
def print_slow(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(0.05)  
print_slow("Chào mừng đến với casino của thằng này\n")
print_slow("=== Game Launcher === \n [1] Tài xỉu \n [2] Roulette \n [3] Thoát")
while True:
    game_play = int(input("\n Chọn game: "))
    if game_play == 1:
                # Chạy sicbo.py trong CMD riêng, từ đúng thư mục
        subprocess.call(
            ["python", "sicbo.py"],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
            cwd="C:\code\sicbo"
        )
    elif game_play == 2:
        subprocess.call(
            ["python", "roulette.py"],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
            cwd="C:\code\sicbo"
        )
    elif game_play == 3:
        print("Tạm biệt!")
        break