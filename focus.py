import subprocess

def focus_window(window_id):
    try:
        # Use xdotool to focus the window by its ID
        subprocess.run(["xdotool", "windowfocus", window_id])
        print(f"Focused window with ID: {window_id}")
    except Exception as e:
        print(f"Error focusing window: {e}")
