from gooey import Gooey, GooeyParser
import imageio
from gooey import options
from glob import glob
import os
import numpy as np
from PIL import Image


def convert(args):
    if args.folder:
        files = glob(os.path.join(args.folder, '*.png'))
        print('Selected folder:', args.folder)
    else:
        files = args.input
        print('Selected files:', args.input)
    size = imageio.imread(files[0]).shape
    print(size[0:2])
    writer = imageio.get_writer(args.output, fps=args.fps, mode='I')
    for img in sorted(files):
        image2 = imageio.imread(img)
        if size != image2.shape:
            im = list(Image.fromarray(
                image2).resize((size[1], size[0])).getdata())
            image2 = np.reshape([list(ele) for ele in im], size)
            print(f'{img} has diferent size - try resize to insert in video')
            print(size)
        writer.append_data(image2)
    writer.close()


@Gooey(program_name='PNG2AVI_GUI v1.1', default_size=(600, 600))
def main():
    parser = GooeyParser(description="Create a movie from png files.")

    png_in = parser.add_mutually_exclusive_group(
        required=True,
        gooey_options=options.MutexGroup(title='All png in directory'))
    png_in.add_argument("--folder", widget="DirChooser")

    png_in.add_argument('--input',
                        default=None,
                        metavar='Input PNG', nargs='*',
                        help='The png for which you want to create avi',
                        gooey_options=dict(wildcard="PNG files (*.png)|*.png"),
                        widget='MultiFileChooser')

    parser.add_argument('fps',
                        metavar='Frames per seconds',
                        default=2, type=float,
                        gooey_options={'visible': True})

    parser.add_argument('output',
                        metavar='Output avi',
                        help='Where to save the video',
                        widget='FileSaver',
                        gooey_options=dict(
                            wildcard="Video file (*.mp4)|*.mp4"),
                        )
    args = parser.parse_args()
    convert(args)


if __name__ == '__main__':
    main()
