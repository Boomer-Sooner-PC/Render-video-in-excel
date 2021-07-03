import os
import cv2

# resizing video
vid = cv2.VideoCapture('video.mp4')
print("Resizing video")
# os.system("ffmpeg -i video.mp4 -vf scale=120:90 resized.mp4")

# converts video to grayscale
print("converting video to grayyscale")
source = cv2.VideoCapture('resized.mp4')
while True:
    ret, img = source.read()  # extract frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    cv2.imshow("Live", gray)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
source.release()
