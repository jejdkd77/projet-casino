import os
import subprocess
import sys
import time

def print_slow(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(0.05)
base_path = os.path.dirname(os.path.abspath(__file__))
print_slow("Welcome to my casino\n")
print_slow("=== Game Launcher === \n [1] Sicbo \n [2] Roulette \n [3] Exit")

while True:
        game_play = int(input("\nChọn game: "))
        if game_play == 1:
            subprocess.call(
                ["python", "sicbo.py"],
                creationflags=subprocess.CREATE_NEW_CONSOLE,
                cwd=base_path
            )
        elif game_play == 2:
            subprocess.call(
                ["python", "roulette.py"],
                creationflags=subprocess.CREATE_NEW_CONSOLE,
                cwd=base_path
            )
        elif game_play == 3:
            print("Bye!")
            break
        else:
            print_slow("doesnt have game with your choice.\n")
