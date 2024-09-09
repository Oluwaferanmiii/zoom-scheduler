import subprocess
import pyautogui
import time
import pyautogui
import pyscreeze
import PIL

print("pyautogui version:", pyautogui.__version__)
print("pyscreeze version:", pyscreeze.__version__)
print("Pillow version:", PIL.__version__)


def start_zoom_meeting():

    zoom_path = r'C:\Users\Admin\AppData\Roaming\Zoom\bin\Zoom.exe'

    try:
        #Open zoom (adjust path if necessary)
        subprocess.Popen(zoom_path)

        time.sleep(5) #Allow zoom to open
        
        time.sleep(2)  # adjust the sleep time according to your system's speed

# Move the mouse to the Join button location
        #pyautogui.moveTo(850, 550)  # adjust the coordinates according to your screen resolution

# Click the Join button
        #pyautogui.click()
        join_button = pyautogui.locateOnScreen(r'C:\Users\Admin\OneDrive\Desktop\zoomclick\join_button.png')
        if join_button is not None:
            pyautogui.click(join_button)
        else:
            print("Join button not found!")
            return
        

        pyautogui.typewrite('#Meetind-id')
        pyautogui.press('enter')
        
        time.sleep(2)
        
        pyautogui.typewrite('#Password')
        pyautogui.press('enter')

    except Exception as e:
        print(f"Error occurred: {str(e)} ")

if __name__ == '__main__':
    start_zoom_meeting()
