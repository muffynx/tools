import os
import pyttsx3
sec = 1800

os.system(f'shutdown /s /t {sec}')
pyttsx3.speak(f"OK sir i'm shutting down your pc in next {sec} seconds")