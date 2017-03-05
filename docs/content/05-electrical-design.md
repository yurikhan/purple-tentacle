Title: Electrical design
Date: 2017-02-26
Summary: The wiring scheme.

## Overview

For reading convenience,
the schematic diagram is presented in three parts,
one part for each half of the matrix
and one part showing controller connection.

<div markdown="1">
<figure>[![][left]][left]
<figcaption>[Left half][left]</figcaption></figure>
<figure>[![][right]][right]
<figcaption>[Right half][right]</figcaption></figure>
<figure>[![][schematic]][schematic]
<figcaption>[Controller connection][schematic]</figcaption></figure>
</div>

[left]: {filename}images/05-electrical-design/left.sch.svg
[right]: {filename}images/05-electrical-design/right.sch.svg
[schematic]: {filename}images/05-electrical-design/schematic.sch.svg

**Note** that the column wires of opposite halves connect,
while the row wires do not.

## Source

These schematics are drawn in KiCad EDA.
The source project is in the `schematic` subdirectory.

The images above
are exported using the <kbd><kbd>File</kbd> | <kbd>Plot</kbd></kbd> command,
SVG format,
color mode,
no border and title block,
<kbd>Plot Current Page</kbd> individually for each page.
Afterwards, the SVG images are cropped using Inkscape.
A `Makefile` is provided.

## Concept

The keyswitches are arranged in a matrix
with 12 semi-rows
by 8 columns.
This allows a maximum of 96 keys
using 20 I/O pins.
(The theoretical maximum for 20 pins is
10×10 = 100 keys,
but 12×8 is a bit nicer to work with.
19 pins are insufficient
because they only allow 10×9 = 90 keys.)

The correspondence between keys and matrix cells
is pretty straightforward.
Note that function keys use the innermost columns.
Also note that the navigation and thumb clusters
are wired in a pseudo-row labeled AZ,
with three bottommost keys
arbitrarily assigned to the three outer columns.

An anti-ghosting diode
is placed in series with each keyswitch.
(See the [Rollover, blocking and ghosting][ghosting] article
on the Deskthority wiki
for details.)

[ghosting]: https://deskthority.net/wiki/Rollover,_blocking_and_ghosting

Keyswitches are wired for *active-low* logic.
That is, in order to read a semi-row,
the firmware pulls the corresponding semi-row pin to the ground,
activates the controller’s internal pull-up resistors
to drive inactive columns high,
and senses which column pins went low
as a result of keys being held down.
Thus, diodes have to be directed
towards semi-row wires.

(Active-high logic
would require pulling inactive columns down,
and the Atmega32U4 does not have internal pull-down resistors.
Without pull-downs,
inactive columns would become indeterminate.)

The eight column wires are connected
to the eight pins on the top edge of the Arduino Micro.
The twelve semi-row wires are connected
to pins on the bottom edge.
This leaves three pins
for the status LEDs.

The `RXLED` (`PB0`) pin is left unused.
In experiments,
it wouldn’t keep its assigned state.

Each LED is connected to a PWM-enabled pin
so that the firmware could control their brightness.
(This ability is currently unused;
the firmware implements its own PWM.)

The `PC7` pin,
also known as pin 13 in Arduino Micro,
normally drives the on-board LED.
The controller bootloader blinks this LED
while it’s working.
Wiring an externally visible LED to this pin
makes it possible to observe this blinking
when plugging the keyboard in
before the actual firmware kicks in.

LEDs are wired for *active-high* logic.
That is, the firmware pulls the LED anode pin to +5 V,
allowing the current
to flow through the LED into the ground.
(This simplifies reasoning about the LED state
in the firmware.)

A current limiting resistor is wired
in series with each LED.
See the [Limiting resistors][resistors] section
in the Bill of Materials
for the resistor value calculation formula.

[resistors]: {filename}03-materials.md#limiting-resistors
