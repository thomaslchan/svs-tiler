#!/usr/bin/env python3
import pyvips
import argparse
import os


def tile_svs(filename, output_directory, prefix):
        image = pyvips.Image.openslideload(filename)

        path = os.path.join(
            output_directory,
            '{}.images'.format(prefix)
        )

        if not os.path.exists(path):
            os.mkdir(path)

        pyvips.Image.dzsave(image, os.path.join(path, channel))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create tiles with DeepZoom file.')
    parser.add_argument(
        '--svs_file',
        help='SVS image to be tiled.')
    parser.add_argument(
        '--output_directory', required=True,
        help='Directory for output')
    parser.add_argument(
        '--prefix', required=True,
        help='Prefix for tile filenames')
    args = parser.parse_args()

    tile_svs(
        filename=args.svs_file,
        output_directory=args.output_directory,
        prefix=args.prefix
    )
