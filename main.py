import os

from openpyxl import Workbook
import videoToFrames
import frameToExcel
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
frameList = videoToFrames.FrameCapture("video.mp4")
print("Done converting video to frames")

i = 0

for path in frameList:
    ws = frameToExcel.frameToExcel(path, ws, i)
    i = i+1
    print(f'Processing frame: {i} / {len(frameList)}')

print("Saving sheet (may take a while)")
wb.save("display.xlsx")
print("done")