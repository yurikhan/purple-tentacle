Title: Bill of materials
Date: 2016-12-10T16:00Z
Summary: Parts you need in order to build a Purple Tentacle.

Here is the list
of parts and materials comprising a Purple Tentacle.
All costs are approximate.
Shipping is not included
as it will vary according to your location.

Proprietary parts are marked with a © symbol.
They are designed and produced
by the [Matias Corporation][matias].
In Europe, check [The Keyboard Company][keyboardco].

[matias]: http://matias.ca/
[keyboardco]: http://www.keyboardco.com/

|Part                                      |Qty|©|Cost≈  |
|------------------------------------------|--:|-|------:|
|[Key switch](#key-switches)               | 94|©|[^1]$25|
|[Keycaps](#keycaps)                       | 94|©|[^2]$50|
|[Palm supports](#palm-supports) (optional)|  1|©|    $50|
|[Controller board](#controller-board)     |  1| |    $20|
|[USB cable](#cable)                       |  1| |     $5|
|[Anti-ghosting diode](#diodes)            | 94| |     $1|
|[Status LED](#status-leds)                |  3| |     $1|
|[Limiting resistor](#limiting-resistors)  |  3| |     $1|
|[Mounting plate](#mounting-plate)         |  1| |     $9|
|[Bottom plate](#bottom-plate)             |  1| |     $6|
|[Spacer](#spacer)                         |  1| |    $15|
|[Top frame](#top-frame) (optional)        |  1| |    $10|
|[Wire](#wire)                            |12 m| |     $1|
|[M3×… bolt](#m3-bolts-and-nuts)           |  7| |     $1|
|[M3 washer](#m3-bolts-and-nuts)           | 14| |     $1|
|[M3 acorn nut](#m3-bolts-and-nuts)        |  7| |     $1|
|[M6×10 bolt](#m6-bolts-and-nuts)          |  4| |     $1|
|[M6 washer](#m6-bolts-and-nuts)           |  4| |     $1|
|[M6 hexagonal nut](#m6-bolts-and-nuts)    |  4| |     $1|
|[Self-adhesive rubber feet](#rubber-feet) |2–5| |     $7|
|**Subtotal (no palm supports)**           | | |**≈$150**|
|**Subtotal**                              | | |**≈$200**|

## Key switches

Purple Tentacle is designed around Matias key switches.
A Cherry MX-based variant is possible
but many adjustments will be required
(different cutout size,
different plate thickness,
possibly different frame thickness).

Matias switches come in three variants:

* Quiet Click (PG155B01 or KS101Q)
* Click (PG155B02 or KS101)
* Quiet Linear (KS102Q)

They are sold in boxes of 200,
at $50 a box.

[^1]: Assuming you build two units,
    or split a box with a friend.

If unsure, choose Quiet Click.

## Keycaps

Matias keycaps are available in black or white;
blank or labeled.
They are made of ABS plastic,
have matte cylindrical surface,
and differ by row.

When choosing,
keep in mind the following considerations:

* The blank sets offered by the Matias Corporation directly
  have more keycaps than any of the labeled sets.
* The blank sets sold by The Keyboard Company,
  on the other hand,
  might not.
  Read the description carefully.
* Labeled sets are tailored
  to the conventional keyboard layout.
  You will be able to put *a* cap on each key,
  but not all labels will make sense.
  For example,
  no set offers a single-unit <kbd>Enter</kbd> keycap.

[Signature Plastics][sp] offers a limited selection
of keycaps with Alps mounts;
these are blank only,
more expensive,
and in various colors and profiles.

[sp]: http://pimpmykeyboard.com/

There is no default for the keycaps;
you have to make this choice.

[^2]: Assuming a Matias keycap set,
    with no Signature Plastics additions.

## Palm supports

Purple Tentacle uses palm supports
designed for the Matias Ergo Pro keyboard.
These come in five colors:
White, Black, Red, Navy Blue, and Astronaut Blue.
They are gel pads covered with silk,
attached to a plastic/steel base.

Whether to use palm supports
is a personal choice,
dependent on your typing habits.

If you do use the palm supports,
they will accumulate lint from your palms.
Once in a while,
detach them
and hand-wash with soap.
Do not put in a washing machine!
Dishwasher compatibility not tested.

## Controller board

For the controller,
choose an Atmel ATmega32u4-based breakout board
which exposes at least 23 I/O pins,
is wired for 5 V,
and is sufficiently small (≈50×20 mm or so).
Possibilities include
(but are not necessarily limited to):

* [Arduino Micro][arduino] or clone
* [Adafruit Atmega32u4 Breakout Board][adafruit]
* [Pololu A-Star 32U4 Mini][astar]
* [PJRC Teensy 2.0][teensy]

[arduino]: https://www.arduino.cc/en/Main/arduinoBoardMicro
[adafruit]: https://www.adafruit.com/products/296
[astar]: https://www.pololu.com/product/3102
[teensy]: https://www.pjrc.com/teensy/index.html

These boards do *not* expose enough pins:

* Pololu A-Star 32U4 Micro (18 pins)
* SparkFun Pro Micro (18 pins)

This instruction assumes Arduino Micro.
For other boards,
minor adjustments to wiring
and/or firmware may be needed.

Note that some boards
will not advertise their total pin number.
For example,
Arduino Micro advertises 20.
For best results,
check the schematic
and count I/O pins
which have no other components attached.

If the board has a pin
that only drives a general-purpose LED,
count it also;
use it for one of the keyboard status LEDs.
(This way you get useful feedback
when the bootloader flashes this LED.)
Avoid pins that drive fixed-purpose LEDs
such as RXLED and TXLED.

Given a choice, prefer boards
that come *without* solderless breadboard pins attached —
they won’t fit in the keyboard case
and you’ll have to desolder them.

## Cable

Choose a cable so
that one end fits the controller board
(either mini or micro USB B male connector)
and the other end has a standard USB A male connector.
Choose a length that fits your working environment.
Avoid ferrite rings
and L-shaped connectors
as they will be a hassle to fit in the keyboard case.

## Diodes

To prevent ghosting,
a diode is installed
in series with each key switch.

This instruction assumes 1N4148 diodes.

## Status LEDs

For status indicators
(Num Lock, Caps Lock, Scroll Lock),
choose LEDs that will
fit in 8 mm space
and have forward voltage of 3 V or less.
Prefer diffused ones.
Choose through-hole mount,
not surface mount.

This instruction assumes ⌀3 mm green LEDs,
forward voltage 1.8–2 V,
maximum current 20 mA.

## Limiting resistors

Calculate the minimum limiting resistor value as
<var>R</var><sub>min</sub> =
(<var>V</var><sub>cc</sub>
− <var>V</var><sub>f</sub>)
/ <var>I</var><sub>max</sub>,
where
<var>V</var><sub>cc</sub> = 5 V,
<var>V</var><sub>f</sub> is the LED forward voltage,
and <var>I</var><sub>max</sub> is the LED maximum current,
and use an actual value above that
in order to keep the current through LEDs within specifications.

For best results,
try resistors of several values
and choose the one that yields the most comfortable LED brightness.
Your goal is to make the LED noticeable
but not painful to look at.
Be sure to test
both in bright daylight
and in dim lighting.

For example,
for the LEDs specified above
the formula gives a minimum resistance of 150 Ω,
but a 1 kΩ value gives a more pleasant brightness.

## Mounting plate

Matias switches are mounted on a plate 1 mm thick.
Ask your laser cutting facility
what materials they carry.

If in doubt,
choose stainless steel.
(If you make a Purple Tentacle
with a plate made of a different material,
please [share your experience][materials]!)

[materials]: https://github.com/yurikhan/purple-tentacle/issues/1

## Bottom plate

The bottom plate covers the electronics from below.
If you choose to use palm supports,
the bottom plate is what they attach to.

This instruction assumes 1 mm stainless steel,
same as the mounting plate.

## Spacer

The spacer is the layer of the case
between the bottom plate and the mounting plate.
It provides outer walls
for the internal cavity
that houses the electronics.

This layer must be at least 9 mm thick.
When key switches are inserted into the mounting plate,
their pin ends will go 8 mm below the plate level,
and you will need a little space
so that the bottom plate does not touch them.

Ask your laser cutter facility
what materials they carry
and what they work with.
If they don’t have anything suitable,
ask what size the raws need to be.

The choice is purely aesthetical.

With translucent plastics,
electronic components next to the edges
will be visible through the case walls.
Also, if your controller board
has an always-on power LED,
it will shine through the back.

This instruction assumes 10 mm clear acrylic.

## Top frame

The top frame provides walls around the keycaps.
It is optional if you do not have kids or pet cats.
If you do, a frame is highly recommended;
otherwise you may find
these can spuriously act
as poorly controlled keycap pullers.

The distance from the mounting plate
to the bottom edge of keycaps
is 8 mm.
On the other end,
experience shows
that a 10 mm frame
makes it difficult to press the thumb base keys.
Therefore, 8 mm thickness is recommended.

The choice of material is mostly aesthetical.
If it is opaque,
you will need holes for the status LEDs.

This instruction assumes 8 mm clear acrylic.

## Wire

Purple Tentacle does not use a PCB;
instead, it is hand-wired.
There are a couple of reasons for that:

* When building a single unit or two,
  manufacturing a board
  is more hassle than hand-wiring.
* Given that switches are inserted
  into the mounting plate
  from above,
  soldering them to a PCB below
  will make it almost impossible
  to replace a faulty switch
  without desoldering the whole board.
  Faulty switches *do* happen,
  and you will discover them
  only after finishing assembly
  and typing for a few hours.

Matrix rows are wired with diode pins;
for everything else you need wire.
If you have soldering experience,
use whichever wire is convenient for you.
(You probably already have a stash of soldering wire.)
If not, choose solid core copper wire,
around AWG 26 (0.13 mm<sup>2</sup>).

Category 5 twisted pair can be used
if that’s what you have handy.
It provides convenient color coding for the wires,
although it is a bit too rigid.
If you go this way,
you need 1.5 m 4-pair UTP
or 3 m 2-pair UTP.

## M3 bolts and nuts

M3 bolts and acorn nuts
screw the case details together.
Washers protect the top frame
against excessive pressure from the nuts.

Choose a bolt length
that is 2 to 4 mm longer
than the total thickness
of the bottom, spacer, plate, and frame (if used).
Add washers if needed.
(The M3 acorn nut has a depth of 4.5 mm.)

For example:
1 mm bottom
+ 10 mm spacer
+ 1 mm plate
+ 8 mm frame
= 20 mm.
The next standard screw length is 25 mm,
which is a bit too long.
The standard M3 washer is 0.5 mm
so we add two of them.

Choose a head shape with a flat underside,
not a countersunk one.

## M6 bolts and nuts

M6 bolts, washers and nuts
are used to attach palm supports.
If you don’t want palm supports,
you can skip these.

The palm supports provide an elevation of ≈8 mm
to the front edge of the keyboard.
This should accommodate most M6 bolt heads
so they won’t scratch your desk.

Choose a head shape with a flat underside,
not a countersunk one.

## Rubber feet

Rubber feet prevent the keyboard from moving on your desk.
Additionally,
they prevent the case bolt heads
from scratching the desk surface.

Choose feet thickness
so that it exceeds the bolt head height.
4 mm or higher
should accommodate most standard shapes of M3 bolt heads.

With palm supports,
two rubber feet are sufficient.
Without palm supports,
you might want five.

The best-known supplier is 3M.
Suitable feet are sometimes bundled
with network appliances such as
switches, home routers, and WiFi access points.
