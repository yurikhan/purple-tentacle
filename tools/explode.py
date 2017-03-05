#!/usr/bin/python3

import argparse
import logging
import math
from math import copysign
import sys

import ezdxf


def parse_args():
    parser = argparse.ArgumentParser(
        description='Explode blocks in a DXF drawing.')
    parser.add_argument('input', metavar='FILE',
        help='input DXF file (“-” for stdin)')
    parser.add_argument('-o', '--output', metavar='FILE',
        help='output file (default: stdout)')
    parser.add_argument('-r', '--recursive', action='store_true',
        help='repeat until no top-level block references remain')
    parser.add_argument('-v', '--verbose', action='count', default=0,
        help='produce debug output')
    return parser.parse_args()


def map_point(point, ref):
    x, y, *_ = point
    dx, dy, *_ = ref.insert
    phi = math.radians(ref.rotation)
    c, s = math.cos(phi), math.sin(phi)
    return (ref.xscale * x * c + ref.yscale * y * -s + dx,
            ref.xscale * x * s + ref.yscale * y * c  + dy,
            0)


def add_other(prototype, layout, ref):
    logging.warning('\t\tUnsupported entity: %s' % prototype.dxftype())


def add_ARC(arc, layout, ref):
    attribs = arc.clone_dxf_attribs()
    del attribs['handle']
    if abs(ref.xscale) != abs(ref.yscale):
        logging.warning('\t\tUnsupported case: '
                        'anisotropic arc scaling (xs=%f, ys=%f)'
                        % (ref.xscale, ref.yscale))
    sa, ea = attribs['start_angle'], attribs['end_angle']
    if ref.xscale < 0:
        sa, ea = math.fmod(540 - ea, 360), math.fmod(540 - sa, 360)
    if ref.yscale < 0:
        sa, ea = 360 - ea, 360 - sa
    rr = attribs['radius'] * abs(ref.xscale)
    layout.add_arc(
        map_point(attribs['center'], ref), rr,
        math.fmod(sa + ref.rotation, 360),
        math.fmod(ea + ref.rotation, 360),
        attribs)


def add_CIRCLE(circle, layout, ref):
    attribs = circle.clone_dxf_attribs()
    del attribs['handle']
    if abs(ref.xscale) != abs(ref.yscale):
        logging.warning('\t\tUnsupported case: '
                        'anisotropic circle scaling (xs=%f, ys=%f)'
                        % (ref.xscale, ref.yscale))
    rr = attribs['radius'] * abs(ref.xscale)
    layout.add_circle(map_point(attribs['center'], ref), rr, attribs)


def add_INSERT(insert, layout, ref):
    attribs = insert.clone_dxf_attribs()
    del attribs['handle']
    attribs['xscale'] *= ref.xscale
    attribs['yscale'] *= ref.yscale
    attribs['rotation'] += ref.rotation
    layout.add_blockref(
        insert.dxf.name, map_point(attribs['insert'], ref), attribs)


def add_LINE(line, layout, ref):
    attribs = line.clone_dxf_attribs()
    del attribs['handle']
    layout.add_line(map_point(attribs['start'], ref),
                    map_point(attribs['end'], ref),
                    attribs)


def add_LWPOLYLINE(lwp, layout, ref):
    attribs = lwp.clone_dxf_attribs()
    del attribs['handle']
    attribs['closed'] = lwp.closed
    logging.debug('scale %f %f', ref.xscale, ref.yscale)
    layout.add_lwpolyline([(xx, yy, sw, ew,
                            copysign(bulge,
                                     bulge * ref.xscale * ref.yscale))
                           for x, y, sw, ew, bulge in lwp.get_points()
                           for xx, yy, *_ in [map_point((x, y), ref)]],
                          attribs)


def explode(d):
    inserts = d.modelspace().query('INSERT')
    if not inserts:
        return False
    for it in inserts:
        logging.debug('%s at %f,%f scale %f,%f rotated %f°'
              % (it.dxf.name, it.dxf.insert[0], it.dxf.insert[1],
                 it.dxf.xscale, it.dxf.yscale, it.dxf.rotation))
        d.modelspace().unlink_entity(it)
        block = d.blocks[it.dxf.name]
        for e in block:
            logging.debug('\t%s' % e.dxftype())
            handler = globals().get('add_%s' % e.dxftype(), add_other)
            handler(e, d.modelspace(), it.dxf)
    return True


def traverse_blocks(d, layout):
    inserts = layout.query('INSERT')
    blocks = {it.dxf.name for it in inserts}
    return blocks.union(*(traverse_blocks(d, d.blocks[name])
                          for name in blocks))


def drop_blocks_except(d, used_blocks):
    to_delete = {b.name for b in d.blocks} - used_blocks
    for name in to_delete:
        if not name.startswith('*') or name.startswith('*D'):
            d.blocks.delete_block(name)


def main():
    args = parse_args()
    logging.basicConfig(format='%(message)s',
                        level=logging.DEBUG if args.verbose >= 1
                        else logging.INFO)
    d = (ezdxf.readfile(args.input) if args.input and args.input != '-'
         else ezdxf.read(sys.stdin))
    modified = explode(d)
    if args.recursive:
        while modified:
            modified = explode(d)
    used_blocks = traverse_blocks(d, d.modelspace())
    drop_blocks_except(d, used_blocks)
    d.saveas(args.output) if args.output else d.write(sys.stdout)


if __name__ == '__main__':
    sys.exit(main())
