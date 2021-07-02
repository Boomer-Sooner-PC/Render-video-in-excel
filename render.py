import time
from natsort import natsorted
import pyautogui
import os
from moviepy.editor import *
import moviepy.video.io.ImageSequenceClip

framesFolder = "frames/"
jumpToLocationX = 45
jumpToLocationY = 175
totalFiles = 0
totalDir = 0

for base, dirs, files in os.walk(framesFolder):
    for Files in files:
        totalFiles += 1

fileNames = []
for i in range(1, totalFiles):
    fileNames.append(f'frames/frame{i}.png')

print("OPEN EXCEL")
# time.sleep(10)

pyautogui.moveTo(jumpToLocationX, jumpToLocationY)

for i in range(1, len(fileNames)):
    pyautogui.click()
    time.sleep(0.2)
    string = f'A{i * 100}'
    pyautogui.typewrite(string)
    pyautogui.hotkey("enter")
    time.sleep(0.2)
    screenshot = pyautogui.screenshot()
    screenshot.save(f'screenshot/frame{i}.png')
    print(f"frame {i} / {len(fileNames)}")

time.sleep(10)
img_array = []
print("Stitching video (could take a while)")

fileNames = []
for i in range(1, totalFiles - 1):
    fileNames.append(f'{os.getcwd()}/screenshot/frame{i}.png')


def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))


lists = list(chunks(fileNames, 100))
i = 0
fps = 10

for image_files in lists:
    print(f'stitching video {i}')
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(f'videos/vid{i}.mp4')
    clip = 0
    i += 1

print("Combining video files")
L = []
for root, dirs, files in os.walk(f'{os.getcwd()}/videos'):
    files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L)
final_clip.to_videofile("output.mp4", fps=10, remove_temp=False)

