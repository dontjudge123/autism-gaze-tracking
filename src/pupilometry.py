import time
import random

def start_pupilometry():
    print("[INFO] Pupilometry session started...")

    for i in range(10):
        diameter = round(random.uniform(2.5, 6.5), 2)
        print(f"Pupil size at t={i}s: {diameter} mm")
        time.sleep(1)

    print("[INFO] Pupilometry session ended.")
