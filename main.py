import pytchat
import time
from pynput.keyboard import Key, Controller
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



keyboard = Controller()


def Move(direction):
    direction = direction.lower()
    if direction == "up":
        keyboard.press(Key.up)
        time.sleep(0.1)
        keyboard.release(Key.up)
    elif direction == "down":
        keyboard.press(Key.down)
        time.sleep(0.1)
        keyboard.release(Key.down)
    elif direction == "right":
        keyboard.press(Key.right)
        time.sleep(0.1)
        keyboard.release(Key.right)
    elif direction == "left":
        keyboard.press(Key.left)
        time.sleep(0.1)
        keyboard.release(Key.left)
    else:
        print("Invalid direction")


def z():
    keyboard.press('z')
    time.sleep(THROTTLE)
    keyboard.release('z')
    
def x():
    keyboard.press('x')
    time.sleep(THROTTLE)
    keyboard.release('x')

def PressEnter():
    keyboard.press(Key.enter)
    time.sleep(.1)
    keyboard.release(Key.enter)


def spliter(msg):
    return msg.lower().split()


commands = [
    UP,
    DOWN,
    RIGHT,
    LEFT,
    ENTER,
    Z,
    X,
]


class LoopController:
    def __init__(self):
        self.flag = True

    def run_loop(self):
        while True:
            try:
                # Focus the game window before interacting with it
                chat = pytchat.create(video_id=VIDEO_ID)
                while chat.is_alive():
                    for c in chat.get().sync_items():
                        if self.flag:
                            focus_window("PokeWilds")
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
    time.sleep(2)
    print("Started...")
    controller = LoopController()
    controller.run_loop()

