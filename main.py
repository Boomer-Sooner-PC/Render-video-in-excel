import genExcelSheet
import render
import reset


print("Please make sure you have all the dependencies installed (look at README.md to see how)")
rdy = input("Do you have all the dependencies installed and a video in this directory names 'video.mp4' (y/n): ")

if rdy == 'y':
    genExcelSheet.main()

    print("Done generating excel spreadsheet, please open the spreadsheet.")
    X = input("What is the X coordinate of the cell select field (github for instructions)")
    Y = input("What is the Y coordinate of the cell select field (github for instructions)")
    rdy = input("Are you ready for it to start taking screenshots? You cannot do anything while it is running. (y/n)")

    if rdy == 'y':
        print("10 seconds to open excel")
        render.main(X, Y)

        print("DONE!")
        reset.main()