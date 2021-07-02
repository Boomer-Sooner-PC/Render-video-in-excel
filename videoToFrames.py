import cv2


def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1
    frameList = []
    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        try:
            cv2.imwrite("frames/frame%d.jpg" % count, image)
            frameList.append("frames/frame%d.jpg" % count)
        except:
            continue
        count += 1
    return frameList
