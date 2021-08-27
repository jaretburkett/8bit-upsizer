import os
import argparse
from PIL import Image


parser = argparse.ArgumentParser()
parser.add_argument("--scale", default=10, type=int, help="Scale to increase file by. 10 = 10x")
args = parser.parse_args()

scale = args.scale

root_folder = os.path.dirname(__file__)
in_folder = os.path.join(root_folder, 'input')
out_folder = os.path.join(root_folder, 'output')


if __name__ == "__main__":
    in_filenames = [f for f in os.listdir(in_folder) if os.path.isfile(os.path.join(in_folder, f))]
    os.makedirs(out_folder, exist_ok=True)

    print(f"Found {len(in_filenames)} files")
    
    for i in range(len(in_filenames)):
        try:
            with Image.open(os.path.join(in_folder, in_filenames[i])) as im:
                im = im.resize([im.width * scale, im.height * scale], resample=Image.NEAREST)
                im.save(os.path.join(out_folder, f"{in_filenames[i]}.png"))
                print(f"SUCCESS - {in_filenames[i]}")
        except:
            print(f"FAILED  - {in_filenames[i]}")

    print("Done")