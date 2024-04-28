import subprocess
import pytchat
import time
import pygetwindow as gw
import pyautogui
import toml
from focus import focus_window

data = toml.load("./config.toml")

# Settings
THROTTLE = data['settings']['throttle']
VIDEO_ID = data['settings']['video_id']

# Commands
UP = data['commands']['up']
DOWN = data['commands']['down']
RIGHT = data['commands']['right']
LEFT = data['commands']['left']
ENTER = data['commands']['enter']
Z = data['commands']['z']
X = data['commands']['x']

game_path = 'pokemon.nds'


def open_game_with_desmume(game_path):
    # Open the game with DeSmuME
    subprocess.Popen(['desmume', game_path])

    # Wait for the emulator to open
    time.sleep(3)  # Adjust the delay as needed

    # Get the window ID of the newly opened DeSmuME window
    wmctrl_output = subprocess.check_output(['wmctrl', '-l', '-x'])
    wmctrl_lines = wmctrl_output.decode('utf-8').split('\n')
    desmume_window_id = None
    for line in wmctrl_lines:
        if 'desmume' in line.lower():  # Adjust for the actual window title
            desmume_window_id = line.split()[0]
            break

    return desmume_window_id


def Move(direction):
    direction = direction.lower()
    if direction == "up":
        pyautogui.press('up')
    elif direction == "down":
        pyautogui.press('down')
    elif direction == "right":
        pyautogui.press('right')
    elif direction == "left":
        pyautogui.press('left')
    else:
        print("Invalid direction")


def z():
    pyautogui.press('z')
    time.sleep(THROTTLE)


def x():
    pyautogui.press('x')
    time.sleep(THROTTLE)


def PressEnter():
    pyautogui.press('enter')
    time.sleep(.1)


def spliter(msg):
    return msg.lower().split()


commands = [UP, DOWN, RIGHT, LEFT, ENTER, Z, X]


class LoopController:
    def __init__(self):
        self.flag = True

    def run_loop(self, desmume_window_id):
        while True:
            try:
                # Activate the target window
                target_window = gw.get_window_by_id(desmume_window_id)
                target_window.activate()

                # Focus the game window before interacting with it
                chat = pytchat.create(video_id=VIDEO_ID)
                while chat.is_alive():
                    for c in chat.get().sync_items():
                        if self.flag:
                            for word in spliter(c.message):
                                if word in commands:
                                    if word == UP:
                                        print("UP")
                                        Move('up')
                                    elif word == DOWN:
                                        print("DOWN")
                                        Move('down')
                                    elif word == RIGHT:
                                        print("RIGHT")
                                        Move('right')
                                    elif word == LEFT:
                                        print("LEFT")
                                        Move('left')
                                    elif word == Z:
                                        print("Z")
                                        z()
                                    elif word == X:
                                        print("X")
                                        x()
                                    elif word == ENTER:
                                        print("ENTER")
                                        PressEnter()
                                    time.sleep(1)
                                else:
                                    time.sleep(0.1)
                                    print('comment not in commands')
            except Exception as e:
                print(f"Error occurred: {e}")
                time.sleep(5)  # Wait for 5 seconds before restarting the loop


if __name__ == "__main__":
    print("Initializing...")
    desmume_window_id = open_game_with_desmume(game_path)
    print("Window ID:", desmume_window_id)
    print("Waiting...")
    time.sleep(120)
    print('Started Game')
    print("Started...")
    controller = LoopController()
    controller.run_loop(desmume_window_id)
