import os, sys, cv2
from glob import glob

###############################################################################
#  USAGE:  python3 vid2frames.py [directory of videos] [path to save frames to]
#  Extracts the frames from a video file and saves them as PNG images.


if len(sys.argv) < 3:
    # shitty way to check if no directory supplied
    print("NOT ENOUGH ARGUMENTS SUPPLIED.")
    print("USAGE:  python3 vid2frames.py [dir of vids] [path to save to]")
    quit()


dir_of_vids = sys.argv[1]   # user input with directory of videos to convert to frames
save_dir = ""

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")


def save_frame(video_path, save_dir, gap=10):
    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    idx = 0

    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break

        if idx == 0:
            cv2.imwrite(f"{save_path}/{idx}.png", frame)
        else:
            if idx % gap == 0:
                cv2.imwrite(f"{save_path}/{idx}.png", frame)

        idx += 1


if len(sys.argv) == 2:
    # no save directory supplied, so set a default one.
    create_dir('save')
    save_dir = "save"
else:
    # otherwise, set it to the user supplied path
    save_dir = sys.argv[2]


if __name__ == "__main__":
    video_paths = glob(str(dir_of_vids) + "/*")

    for path in video_paths:
        save_frame(path, save_dir, gap=10)
