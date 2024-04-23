game_path = 'pokemon.nds'
import subprocess
import time
import pyautogui

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

# Example usage

window_id = open_game_with_desmume(game_path)
print("Window ID:", window_id)

# Example interaction with the window using PyAutoGUI
if window_id:
    # Activate the DeSmuME window
    subprocess.call(['wmctrl', '-ia', window_id])
    
    # Example interaction - click at a specific location on the window
    # You may need to adjust the coordinates based on your game's U
    # Wait for 1 minute
    print('Waiting,,')
    time.sleep(60)

    # Close the window
    subprocess.call(['wmctrl', '-ic', window_id])
