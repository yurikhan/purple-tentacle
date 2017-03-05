#!/usr/bin/python3

import argparse
import logging
import math
from math import copysign
import sys

import ezdxf
import svgwrite


class Bounds:
    def __init__(self):
        self.minx = None
        self.miny = None
        self.maxx = None
        self.maxy = None

    def extend(self, minx, miny, maxx, maxy):
        self.minx = minx if self.minx is None else min(self.minx, minx)
        self.miny = miny if self.miny is None else min(self.miny, miny)
        self.maxx = maxx if self.maxx is None else max(self.maxx, maxx)
        self.maxy = maxy if self.maxy is None else max(self.maxy, maxy)

    def viewBox(self, padding=0):
        return '%f %f %f %f' % (
            self.minx - padding, self.miny - padding,
            self.maxx - self.minx + 2 * padding,
            self.maxy - self.miny + 2 * padding)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Export a flattened DXF drawing as an SVG image. '
        'Assumes no blocks or layers. '
        'Only simple shapes are supported.')
    parser.add_argument('input', metavar='FILE',
        help='input DXF file (“-” for stdin)')
    parser.add_argument('-o', '--output', metavar='FILE',
        help='output SVG file (default: stdout)')
    parser.add_argument('-v', '--verbose', action='count', default=0,
        help='produce debug output')
    return parser.parse_args()


def point(dxf_point):
    x, y, *_ = dxf_point
    return (x, -y)


def add_other(e, svg, bounds):
    logging.warning('%s not supported', e.dxftype())


def add_ARC(a, svg, bounds):
    cx, cy = point(a.dxf.center)
    r = a.dxf.radius
    sa = math.radians(a.dxf.start_angle)
    ea = math.radians(a.dxf.end_angle)
    path = svg.path(('M', (cx + r * math.cos(sa),
                           cy - r * math.sin(sa))))
    path.push_arc((cx + r * math.cos(ea), cy - r * math.sin(ea)),
                  0, r, large_arc=ea - sa > math.pi, angle_dir='-', absolute=True)
    svg.add(path)
    bounds.extend(cx - r, cy - r, cx + r, cy + r)


def add_CIRCLE(c, svg, bounds):
    cx, cy = point(c.dxf.center)
    r = c.dxf.radius
    svg.add(svg.circle((cx, cy), r))
    bounds.extend(cx - r, cy - r, cx + r, cy + r)


def add_LINE(l, svg, bounds):
    x0, y0 = point(l.dxf.start)
    x1, y1 = point(l.dxf.end)
    svg.add(svg.line(start=(x0, y0), end=(x1, y1)))
    bounds.extend(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))


def add_LWPOLYLINE(lwp, svg, bounds):
    points = list(lwp.get_points())
    if not points:
        return
    if lwp.closed:
        points.append(points[0])
    x0, y0 = point(points[0])
    path = svg.path(('M', (x0, y0)))
    bounds.extend(x0, y0, x0, y0)
    for ((x0, y0, _, _, bulge),
         (x, y, sw, ew, _)) in zip(points, points[1:]):
        xx0, yy0 = point((x0, y0))
        xx, yy = point((x, y))
        if bulge == 0:
            path.push('L', (xx, yy))
            bounds.extend(xx, yy, xx, yy)
        else:
            d = ((xx - xx0)**2 + (yy - yy0)**2)**0.5 / 2
            a = 4 * math.atan(bulge)
            r = d * (bulge**2 + 1) / (2 * abs(bulge))
            path.push_arc((xx, yy), 0, r,
                          large_arc=abs(a) > math.pi,
                          angle_dir='+' if a < 0 else '-',
                          absolute=True)
            bounds.extend(xx - r, yy - r, xx + r, yy + r)
    svg.add(path)


def export(d):
    entities = d.modelspace().query('*')
    bounds = Bounds()
    svg = svgwrite.Drawing()
    svg.add(svg.style('\n'.join((
        'svg {',
        '  stroke: black;'
        '  stroke-width: 0.25;'
        '  fill: none;'
        '}'))))
    for e in entities:
        handler = globals().get('add_%s' % e.dxftype(), add_other)
        handler(e, svg, bounds)
    svg['viewBox'] = bounds.viewBox(10)
    return svg


def main():
    args = parse_args()
    logging.basicConfig(format='%(message)s',
                        level=logging.DEBUG if args.verbose
                        else logging.INFO)
    d = (ezdxf.readfile(args.input) if args.input and args.input != '-'
         else ezdxf.read(sys.stdin))
    svg = export(d)
    svg.saveas(args.output) if args.output else svg.write(sys.stdout)


if __name__ == '__main__':
    sys.exit(main())
