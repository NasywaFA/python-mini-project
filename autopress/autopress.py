from pynput.keyboard import Key, Controller, Listener
import threading
import time

keyboard = Controller()
pressing = False

def print_instructions():
    print("=" * 50)
    print(" AUTO KEY PRESSER — READY")
    print("=" * 50)
    print("Key:        W")
    print("Mode:       Auto Press")
    print("")
    print("Controls:")
    print("  F6   → Start / Stop auto pressing")
    print("  ESC  → Exit program")
    print("")
    print("Status:     Waiting for input...")
    print("=" * 50)
    print()

def auto_press():
    while True:
        if pressing:
            keyboard.press('w')
            keyboard.release('w')
            time.sleep(0.05) # press speed (the smaller the number, the faster the speed)

def on_press(key):
    global pressing
    # F6 = toggle start/stop
    if key == Key.f6:
        pressing = not pressing
        print(f"[INFO] Auto press {'ENABLED' if pressing else 'DISABLED'}")
    
    # ESC = keluar program
    elif key == Key.esc:
        print("[INFO] Program terminated.")
        return False

print_instructions()

threading.Thread(target=auto_press, daemon=True).start()

with Listener(on_press=on_press) as listener:
    listener.join()