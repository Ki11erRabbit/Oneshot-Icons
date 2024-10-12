import argparse
import os
import subprocess
import sys


colors = {
        'purple': '#9664ff',
        'blue': '#746BE6',
        'cyan': '#35CDD2',
        'green': '#3FD564',
        'yellow': '#FFD26A',
        'red': '#D5216A',
        'white': '#FFFFFF',
        'pink': '#FE55BF',
        'orange': '#FD8F4D',
        }
#todo: add remaining colors


output_dir = "oneshot_icons"
source_dir = "src"
icon_sizes = [16, 32, 48, 64, 128, 256, 512]

def create_icon(size, color, file_type):
    if os.path.exists(f"{output_dir}/{size}x{size}"):
        print(f"Icon {size}x{size} already exists.")
        return
    else:
        os.makedirs(f"{output_dir}/{size}x{size}")

    for file in os.listdir(source_dir):
        if not os.path.exists(f"{os.getcwd()}/{source_dir}/{file}/convert.sh"):
            continue
        if not os.path.exists(f"{os.getcwd()}/{output_dir}/{size}x{size}/{file}"):
            os.makedirs(f"{os.getcwd()}/{output_dir}/{size}x{size}/{file}")
        program = ['./convert.sh', str(size), color, file_type, f"{os.getcwd()}/{output_dir}/{size}x{size}/{file}"]
        proc = subprocess.Popen(program, cwd=f"{os.getcwd()}/{source_dir}/{file}")
        proc.wait()

def create_scallable_icon(color):
    if os.path.exists(f"{output_dir}/scalable"):
        print(f"Icon scalable already exists.")
        return
    else:
        os.makedirs(f"{output_dir}/scalable")

    for file in os.listdir(source_dir):
        if not os.path.exists(f"{os.getcwd()}/{source_dir}/{file}/convert.sh"):
            continue
        if not os.path.exists(f"{os.getcwd()}/{output_dir}/scalable/{file}"):
            os.makedirs(f"{os.getcwd()}/{output_dir}/scalable/{file}")
        program = ['./convert.sh', '128', color, 'svg', f"{os.getcwd()}/{output_dir}/scalable/{file}"]
        proc = subprocess.Popen(program, cwd=f"{os.getcwd()}/{source_dir}/{file}")
        proc.wait()


def main(args):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if args.size is None:
        sizes = icon_sizes
    else:
        sizes = [args.size]

    color = colors[args.color]

    for size in sizes:
        create_icon(size, color, 'png')

    create_scallable_icon(color)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', type=int, default=None)
    parser.add_argument('-c', '--color', default='purple')
    args = parser.parse_args()
    main(args)
