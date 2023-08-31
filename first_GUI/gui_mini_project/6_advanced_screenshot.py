import time
import keyboard
from PIL import ImageGrab

def screenshot():
    #   2023Y 8M 31D 10H 20M 25S ->_20230831_102025
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png" .format(curr_time))  # image_20230831_102025.png

keyboard.add_hotkey('F9', screenshot)   # 사용자가 F9 키를 누르면 스크린 샷 저장
# keyboard.add_hotkey('a', screenshot)   # 사용자가 'a' 키를 누르면 스크린 샷 저장
# keyboard.add_hotkey('ctrl+shift+s', screenshot)   
# # 사용자가 'ctrl + shift + s' 키를 누르면 스크린 샷 저장

keyboard.wait("esc")    # 사용자가 esc를 누를 때까지 프로그램 수행

