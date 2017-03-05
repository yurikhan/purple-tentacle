#!/usr/bin/python3

import argparse
import logging
import math
from math import copysign
import sys

import ezdxf


def parse_args():
    parser = argparse.ArgumentParser(
        description='Export a subset of layers from a DXF drawing, '
        'flattened in a single layer. Assumes no blocks.')
    parser.add_argument('input', metavar='FILE',
        help='input DXF file (“-” for stdin)')
    parser.add_argument('layers', metavar='LAYER', nargs='*',
        help='layers to export (default: all); '
        'other layers will be dropped')
    parser.add_argument('-o', '--output', metavar='FILE',
        help='output file (default: stdout)')
    parser.add_argument('-v', '--verbose', action='count', default=0,
        help='produce debug output')
    return parser.parse_args()


def flatten(d, layers):
    entities = d.modelspace().query('*')
    for e in entities:
        if not layers or e.dxf.layer in layers:
            e.dxf.layer = '0'
        else:
            d.modelspace().delete_entity(e)
    to_remove = {l.dxf.name for l in d.layers} - {'0'}
    logging.debug(to_remove)
    for name in to_remove:
        d.layers.remove(name)


def main():
    args = parse_args()
    logging.basicConfig(format='%(message)s',
                        level=logging.DEBUG if args.verbose
                        else logging.INFO)
    d = (ezdxf.readfile(args.input) if args.input and args.input != '-'
         else ezdxf.read(sys.stdin))
    flatten(d, args.layers)
    d.saveas(args.output) if args.output else d.write(sys.stdout)


if __name__ == '__main__':
    sys.exit(main())
