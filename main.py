from src.gaze_tracker import start_gaze_tracking
from src.pupilometry import start_pupilometry

if __name__ == "__main__":
    print("Starting Autism Gaze Tracking App...\n")

    start_gaze_tracking()

    start_pupilometry()
