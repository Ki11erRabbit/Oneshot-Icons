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

index_theme_start = """[Icon Theme]
Name=Oneshot Icons
Comment=Icons inspired by the ui in Oneshot: World Machine Edition
Inherits=Mint-Y

Example=folder

"""

output_dir = "oneshot_icons"
source_dir = "src"
icon_sizes = [16, 32, 48, 64, 128, 256, 512]
cursor_sizes = [24, 32, 48, 64, 72, 120, 144, 240]
directory_list = "Directories="


def attach_context(output, file):
    output += "\n"
    match file:
        case 'emblems':
            output += f"Context=Emblems"
        case 'actions':
            output += f"Context=Actions"
        case 'apps':
            output += f"Context=Applications"
        case 'categories':
            output += f"Context=Categories"
        case 'devices':
            output += f"Context=Devices"
        case 'emotes':
            output += f"Context=Emotes"
        case 'mimetypes':
            output += f"Context=MimeTypes"
        case 'panel':
            output += f"Context=Status"
        case 'places':
            output += f"Context=Places"
        case 'status':
            output += f"Context=Status"
        case 'symbolic':
            output += f"Context=Symbolic"
    return output


def create_icon(size, color, file_type):
    if os.path.exists(f"{output_dir}/{size}x{size}"):
        print(f"Icon {size}x{size} already exists.")
        return
    else:
        os.makedirs(f"{output_dir}/{size}x{size}")
    
    output = ""

    for file in os.listdir(source_dir):
        if not os.path.exists(f"{os.getcwd()}/{source_dir}/{file}/convert.sh"):
            continue
        if not os.path.exists(f"{os.getcwd()}/{output_dir}/{size}x{size}/{file}"):
            os.makedirs(f"{os.getcwd()}/{output_dir}/{size}x{size}/{file}")
        program = ['./convert.sh', str(size), color, file_type, f"{os.getcwd()}/{output_dir}/{size}x{size}/{file}"]
        proc = subprocess.Popen(program, cwd=f"{os.getcwd()}/{source_dir}/{file}")
        proc.wait()

        output += f"\n[{size}x{size}/{file}]"
        output = attach_context(output, file)
        output += f"\nSize={size}\nType=Fixed\n"
        
        global directory_list
        directory_list += f"{size}x{size}/{file},"

        for subfile in os.listdir(f"{os.getcwd()}/{output_dir}/{size}x{size}/{file}"):
            if !subfile.endswith(file_type):
                output += f"\n[{size}x{size}/{file}/{subfile}]"
                output = attach_context(output, file)
                directory_list += f"{size}x{size}/{file}/{subfile},"

    return output

def create_scallable_icon(color):
    if os.path.exists(f"{output_dir}/scalable"):
        print(f"Icon scalable already exists.")
        return
    else:
        os.makedirs(f"{output_dir}/scalable")

    output = ""

    for file in os.listdir(source_dir):
        if not os.path.exists(f"{os.getcwd()}/{source_dir}/{file}/convert.sh"):
            continue
        if not os.path.exists(f"{os.getcwd()}/{output_dir}/scalable/{file}"):
            os.makedirs(f"{os.getcwd()}/{output_dir}/scalable/{file}")
        program = ['./convert.sh', '128', color, 'svg', f"{os.getcwd()}/{output_dir}/scalable/{file}"]
        proc = subprocess.Popen(program, cwd=f"{os.getcwd()}/{source_dir}/{file}")
        proc.wait()

        output += f"\n[scalable/{file}]"
        output = attach_context(output, file)
        output += f"\nMinSize=16\nMaxSize=1024\nType=Scalable\n"
        
        global directory_list
        directory_list += f"scalable/{file},"

        for subfile in os.listdir(f"{os.getcwd()}/{output_dir}/scalable/{file}"):
            if !subfile.endswith('svg'):
                output += f"\n[scalable/{file}/{subfile}]"
                output = attach_context(output, file)
                directory_list += f"scalable/{file}/{subfile},"

    return output

def create_cursor(size):
    if os.path.exists(f"{output_dir}/cursors/"):
        print("Icon cursors already exists.")
        return
    else:
        os.makedirs(f"{output_dir}/cursors/")

    program = ['./convert-cursor.sh', str(size), f"{os.getcwd()}/{output_dir}/cursors/"]
    proc = subprocess.Popen(program, cwd=f"{os.getcwd()}/{source_dir}/cursors")
    proc.wait()
    program = ['python', f'{os.getcwd()}/create_cursor.py', f'{size}']
    proc = subprocess.Popen(program, cwd=f"{os.getcwd()}/{output_dir}/cursors/")
    proc.wait()



def main(args):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if args.size is None:
        sizes = icon_sizes
    else:
        sizes = [args.size]

    color = colors[args.color]

    icon_configs = []

    for size in sizes:
        icon_configs.append(create_icon(size, color, 'png'))

    icon_configs.append(create_scallable_icon(color))
    create_cursor(args.cursor_size)

    global directory_list
    directory_list = directory_list[:-1] + "\n"
    with open(f"{output_dir}/index.theme", 'w') as f:
        f.write(index_theme_start)
        f.write(directory_list)
        for config in icon_configs:
            f.write(config)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', type=int, default=None)
    parser.add_argument('-cs', '--cursor_size', type=int, default=48)
    parser.add_argument('-c', '--color', default='purple')
    args = parser.parse_args()
    main(args)
