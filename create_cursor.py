import argparse
import os
import subprocess


class CursorConf:
    def __init__(self, size, x, y, name, x11_name, x11_links, files, refresh_rate=1000):
        self.size = size
        self.x = x #* size
        self.y = y #* size
        self.name = name
        self.x11_name = x11_name
        self.x11_links = x11_links
        self.files = files
        self.refresh_rate = refresh_rate
    
    def write_conf(self):
        with open(f'{self.x11_name}.in', 'w') as f:
            for link in self.files:
                f.write(f'{self.size} {self.x} {self.y} {link} {self.refresh_rate}\n')

    def create_symlink(self):
        for link in self.x11_links:
            os.symlink(f'{self.x11_name}', link)
    
    def create_cursor(self):
        self.write_conf()
        process = subprocess.Popen(['xcursorgen', f'{self.x11_name}.in', f'{self.x11_name}'])
        self.create_symlink()
    
    def clean_up(self):
        for file in self.files:
            try:
                os.remove(file)
            except FileNotFoundError:
                continue
        os.remove(f'{self.x11_name}.in')




def main(args):
    size = args.size

    cursors = [
            CursorConf(size, 6, 6, '', 'all-scroll', ['fleur', 'size_all'], ['move.png']),
            CursorConf(size, 5, 5, 'Diagonal_1', 'bd_double_arrow', ['c7088f0f3e6c8088236ef8e1e3e70000', 'nw-resize', 'nwse-resize', 'size_fdiag', 'se-resize'], ['size_NwSe.png']),
            CursorConf(size, 0, 12, '', 'bottom_left_corner', [], ['bottom_left_corner.png']),
            CursorConf(size, 12, 12, '', 'bottom_right_corner', [], ['bottom_right_corner.png']),
            CursorConf(size, 5, 9, '', 'bottom_side', [], ['bottom_side.png']),
            CursorConf(size, 7, 0, '', 'center_ptr', [], ['arrow-center.png']),
            CursorConf(size, 6, 3, '', 'col-resize', ['split_h'], ['size_ew.png']),
            CursorConf(size, 0, 5, '', 'color-picker', [], ['color-picker.png']),
            CursorConf(size, 0, 0, '', 'context-menu', [], ['context-menu.png']),
            CursorConf(size, 6, 7, '', 'copy', ['1081e37283d90000800003c07f3ef6bf', '6407b0e94181790501fd1e167b474872', 'b66166c04f8c3109214a4fbd64a50fc8', 'dnd-copy'], ['grab.png']),
            CursorConf(size, 4, 4, 'Cross', 'cross', ["cross_reverse", "diamond_cross", "tcross", "crosshair"], ['precise.png']),
            CursorConf(size, 5, 5, 'Unavailiable', 'dnd_no_drop', ["03b6e0fcb3499374a867c041f52298f0", "circle", "dnd-no-drop", "no-drop"], ['forbidden.png']),
            CursorConf(size, 3, 3, '', 'dotbox', ["dot_box_mask", "draped_box", "icon", "target"], ['dotbox.png']),
            CursorConf(size, 5, 5, 'Diagonal_2', 'fd_double_arrow', ["fcf1c3c7cd4491d801f1e1c78f100000", "ne-resize", "nesw-resize", "sw-resize","size_bdiag"], ['size_NeSw.png']),
            CursorConf(size, 6, 6, 'Move', 'hand1', ["grab", "openhand"], ['openhand.png']),
            CursorConf(size, 6, 6, 'Link', 'hand2', ["9d800788f1b08800ae810202380a0822", "e29285e634086352946a0e7090d73106", "pointer", "pointing_hand"], ['pointer1.png', 'pointer2.png'], refresh_rate=500),
            CursorConf(size, 0, 0, 'Default', 'left_ptr', ['arrow', 'default', 'top_left_arrow'], ['arrow.png']),
            CursorConf(size, 0, 0, 'Work', 'left_ptr_watch', ["00000000000000020006000e7e9ffc3f", "08e8e1c95fe2fc01f976f1e063a24ccd", "3ecb610c1bf2410f44200f48c40d3599", "progress"], ['background.png']),
            CursorConf(size, 2, 6, '',  'left_side', [], ['left_side.png']),
            CursorConf(size, 6, 6, '',  'move', ["4498f0e0c1937ffe01fd06f973665830", "9081237383d90e509aa00f00170e968f","fcf21c00b30f7e3f83fe0dfd12e71cff", "grabbing", "pointer_move", "dnd-move", "closedhand", "dnd-none"], ['grab.png']),
            CursorConf(size, 0, 0, 'Handwriting',  'pencil', ['draft'], ['pen.png']),
            CursorConf(size, 5, 5, '', 'pirate', [], ['forbidden.png']),
            CursorConf(size, 3, 3, '', 'plus', ['cell'], ['plus.png']),
            CursorConf(size, 0, 0, 'Help', 'question_arrow', ["5c6cd98b3f3ebcb1f9c7f1c204630408", "d9ce0ab605698f320427677b458ad60b", "help", "left_ptr_help", "whats_this", "dnd-ask"], ['help.png']),
            CursorConf(size, 12, 0, 'Alternate', 'right_ptr', ['draft_large', 'draft_small'], ['arrow-right.png']),
            CursorConf(size, 9, 6, '',  'right_side', [], ['right_side.png']),
            CursorConf(size, 3, 6, '',  'row-resize', ['split_v'], ['size_NS.png']),
            CursorConf(size, 3, 2, '',  'sb_down_arrow', ['down-arrow'], ['down-arrow.png']),
            CursorConf(size, 6, 3, 'Horizontal',  'sb_h_double_arrow', ["028006030e0e7ebffc7f7070c0600140", "14fef782d02440884392942c1120523", "e-resize", "ew-resize", "h_double_arrow", "size-hor", "size_hor", "w-resize"], ['size_ew.png']),
            CursorConf(size, 3, 3, '',  'sb_left_arrow', ['left-arrow'], ['left-arrow.png']),
            CursorConf(size, 3, 3, '',  'sb_right_arrow', ['right-arrow'], ['right-arrow.png']),
            CursorConf(size, 3, 2, '',  'sb_up_arrow', ['up-arrow'], ['up-arrow.png']),
            CursorConf(size, 3, 6, 'Vertical',  'sb_v_double_arrow', ["00008160000006810000408080010102", "2870a09082c103050810ffdffffe0204", "double_arrow", "n-resize", "ns-resize", "size-ver", "size_ver", "s-resize", "v_double_arrow"], ['size_NS.png']),
            CursorConf(size, 0, 0, '',  'top_left_corner', [], ['top_left_corner.png']),
            CursorConf(size, 12, 0, '',  'top_right_corner', [], ['top_right_corner.png']),
            CursorConf(size, 5, 2, '',  'top_side', [], ['top_side.png']),
            CursorConf(size, 5, 5, '',  'vertical-text', [], ['beam-vertical.png']),
            CursorConf(size, 4, 4, 'Busy',  'wait', ['watch'], ['watch.png']),
            CursorConf(size, 0, 0, '', 'wayland-cursor', [], ['wayland.png']),
            CursorConf(size, 0, 0, '', 'X_cursor', ['x-cursor'], ['x_cursor.png']),
            CursorConf(size, 3, 5, 'IBeam',  'xterm', ['ibeam', 'text'], ['beam.png']),
            CursorConf(size, 7, 3, '', 'zoom-in', [], ['zoom-in.png']),
            CursorConf(size, 7, 3, '', 'zoom-out', [], ['zoom-out.png']),
            ]

    for cursor in cursors:
        cursor.create_cursor()
        print(f'Created cursor {cursor.name} with size {cursor.size} at {cursor.x}, {cursor.y}.')

    for cursor in cursors:
        cursor.clean_up()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('size', type=int, help='Size of the cursor')
    args = parser.parse_args()
    main(args)


