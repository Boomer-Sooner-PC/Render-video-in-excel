import os


def main():
    dirs = ['/frames', '/screenshot', '/videos']
    files = ['video.mp4', 'display.xlsx', 'resized.mp4']

    def delete():
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

    inp = input("Are you sure you want to delete all the files (not including the python scripts or output.mp4) (y/n)")
    if inp == "y":
        delete()
    else:
        print("cancelled")


if __name__ == "__main__":
    main()
