Title: Case designs
Date: 2017-01-27
Summary: The sandwich case.

## Overview

The case consists of four parts,
bottom to top:

<div markdown="1">
<figure>[![][bottom]][bottom]
<figcaption>[Bottom plate][bottom]</figcaption></figure>
<figure>[![][spacer]][spacer]
<figcaption>[Spacer][spacer]</figcaption></figure>
<figure>[![][plate]][plate]
<figcaption>[Mounting plate][plate]</figcaption></figure>
<figure>[![][frame]][frame]
<figcaption>[Top frame][frame]</figcaption></figure>
</div>

[bottom]: {filename}/images/04-case-designs/bottom.svg
[spacer]: {filename}/images/04-case-designs/spacer.svg
[plate]: {filename}/images/04-case-designs/plate.svg
[frame]: {filename}/images/04-case-designs/frame.svg

Seven M3 bolts with nuts
hold the parts together.

Palm supports are attached to the bottom plate
with M6 bolts and nuts.
The nuts are held in place
by the hexagonal cutouts in the spacer.

DXF files suitable for laser cutting
are available [from the project repository][dxfs].

[dxfs]: https://github.com/yurikhan/purple-tentacle/case/

## Source files

The remainder of this page
is only important
if you want to modify the physical layout.

This instruction assumes
you have the following software installed:

* LibreCAD

* Python 3

    * Additional packages
      listed in [`requirements.txt`][req].
      You should be able to install them with:

            $ pip3 install --user --requirement requirements.txt

* GNU Make

The preferred source for the case design
is the `master.dxf` file.
It uses blocks to make the design more flexible
and layers to separate case details.

After you modify the master drawing,
run `make all` in the `case` directory.
This will update the individual part DXFs
and images for this instruction.

[req]: https://github.com/yurikhan/purple-tentacle/tools/requirements.txt

## Table of Contents

[TOC]

### Layers

#### 0

The default layer.
Inserts of blocks go here.

#### Bottom, Spacer, Plate, and Frame

Contours that are unique to the named part.

#### Case upper

Contours common to the mounting plate and frame.

#### Case lower

Contours common to the bottom plate and spacer.

#### Case

Common contours of all details.

#### Keycaps

Rectangles for each keycap,
to aid the construction of cutouts in the top frame.

#### Palm supports

Schematics of the palm supports,
to aid in placing the attachment holes.

#### Construction: *

Several layers with auxiliary construction lines
which explain how features are placed.

#### Labels

Sizes, distances, offsets, and rounding radii.

### Blocks

#### Keyswitch cutout

A cutout for one keyswitch.
Change this if you plan to build a Cherry MX-based board.

#### Key

A [keyswitch cutout](#keyswitch-cutout)
and a single 1-unit keycap (19×19 mm).

#### Frame Key

A frame cutout for a single 1-unit [key](#key).

#### Key 1.5

A [keyswitch cutout](#keyswitch-cutout)
and a 1.5-unit keycap,
for the thumb base keys.

#### Frame Key 1.5

A frame cutout for a single [1.5-unit key](#key-1.5).

#### Frame Fgroup

A frame cutout for a horizontal row of four keys.

#### Fgroup

Four [key](#key)s in a horizontal row,
with a [frame cutout](#frame-fgroup),
for function keys.

#### Fkeys

Three [Fgroup](#fgroup)s,
plus two single [key](#key)s on the sides
with corresponding [frame cutout](#frame-key)s.

#### Column

Four [key](#key)s in a vertical column,
grouped so that you could easily adjust column staggering
in the [Hand](#hand) block.

#### Columns

Eight [column](#column)s
arranged according to column stagger.

If you ever need to adjust the column staggering pattern,
this is the place to do it.
It will be mirrored symmetrically.

#### Diamond

Four [key](#key)s in a diamond shape,
for navigation clusters.

#### Thumb cluster

Three 1-unit [key](#key)s
and a single [1.5-unit key](#key-1.5)
with a frame cutout,
for thumb clusters.

#### Hand

Combines the [columns](#columns),
a navigation cluster [diamond](#diamond),
and a [thumb cluster](#thumb-cluster).

#### LED

A 3 mm hole for a single LED.

If you use an opaque material for the top frame,
move the hole from the *Plate* layer
to the *Case upper* layer.

#### LEDs

Three [LED](#led) blocks in a vertical column.

The default LED spacing
is one unit (19 mm).

#### Case screw

A hole for an M3 bolt through all layers.

#### Palm support

* *Palm supports* layer:
  A schematic of the palm support.
* *Bottom* layer:
  Two holes for M6 bolts,
  coinciding with the mounting holes
  on the palm support base.
* *Spacer* layer:
  Cutouts for two hexagonal M6 nuts.

#### Main drawing

Combines the major blocks into a whole:

* [Function key bar](#fkeys)
* Two symmetrical [hand](#hand) blocks,
  each rotated about the origin
  by half the split angle
* [LEDs](#leds)
* [Case screw](#case-screw) holes
* [Palm rest](#palm-rest) attachment holes

This is also where all the manually constructed contours go:

* Frame cutout for the main block
* Exterior boundary
* Spacer cutout

Unfortunately, it’s not easy to automate these.
If you change the matrix,
you will have to re-construct them.
Open a copy of the original drawing alongside
and follow the hints in the *Construction* layers.
