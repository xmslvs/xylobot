from PIL import ImageGrab
import win32gui
import time

def take_screenshot():
    toplist, winlist = [], []
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_cb, toplist)

    obs_preview = [(hwnd, title) for hwnd, title in winlist if 'projector' in title.lower()]
    # just grab the hwnd for first window matching firefox
    hwnd = obs_preview[0][0]
    print(obs_preview)

    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    print(bbox)
    bbox = scale_bbox(bbox)
    time.sleep(0.1)
    img = ImageGrab.grab(bbox, all_screens=True)
    print(bbox)
    img.save("current_screen.png")

def scale_bbox(bbox): #adjusting params to track projection properly across my multiple-monitor setup
    bbox = list(bbox)
    left = bbox[0]
    top = bbox[1]
    right = bbox[2]
    bottom = bbox[3]
    if left >= 1463: 
        right =  left * 1.25 + (right - left) * 1.5
        left *= 1.25
        top *= 1.5
        bottom *= 1.5
    elif top >= 1152:
        left *= 1.25
        top *= 1.25
        right *= 1.25
        bottom *= 1.25
    else:
        left *= 1.75
        top *= 1.75
        right *= 1.75 
        bottom *= 1.75
    bbox = tuple([left, top, right, bottom])
    return bbox