import os

dirs = ['/frames', '/screenshot', '/videos']
files = ['output.mp4', 'video.mp4', 'display.xlsx']


def main():
    for path in dirs:
        path = f'{os.getcwd()}{path}'
        for file in os.listdir(path):
            os.remove(os.path.join(path, file))
    for file in files:
        try:
            file = f'{os.getcwd()}/{file}'
            os.remove(file)
        except:
            continue

inp = input("Are you sure you want to delete all the files (not including the python scripts) (y/n)")
if inp == "y":
    main()
else:
    print("cancelled")
