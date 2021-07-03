import os
from openpyxl import Workbook
import videoToFrames
import frameToExcel
from PIL import Image

def main():
    print("resizing video")
    os.system("ffmpeg -i video.mp4 -vf scale=120:90 resized.mp4")
    wb = Workbook()
    ws = wb.active

    # scales all the columns
    print("Setting up excel sheet")
    rows = []
    for row in ws.iter_cols(1, 120):
        rows.append(str(row).replace("(<Cell 'Sheet'.", "").replace("1>,)", ""))

    for row in rows:
        ws.column_dimensions[row].width = 2.5

    # convert video to frames
    print("Converting video to frames")
    frameList = videoToFrames.FrameCapture("resized.mp4")
    print("Converting frames to grayscale")

    for i in range(0, len(frameList) - 1):
        image = Image.open(f'frames/frame{i}.jpg').convert("L")
        image.save(f'frames/frame{i}.jpg')

    i = 0

    # adds the frames to an excel sheet

    print("Adding frames to excel")

    for path in frameList:
        ws = frameToExcel.frameToExcel(path, ws, i)
        i = i + 1
        print(f'Processing frame: {i} / {len(frameList)}')

    print("Saving sheet (may take a while)")
    wb.save("display.xlsx")
    print("done")


if __name__ == "__main__":
    main()
