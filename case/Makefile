FLATTEN = ../tools/flatten.py
EXPLODE = ../tools/explode.py
TOSVG = ../tools/tosvg.py
SVGDIR = ../docs/content/images/04-case-designs
DXFS = bottom.dxf spacer.dxf plate.dxf frame.dxf
SVGS = $(DXFS:%.dxf=$(SVGDIR)/%.svg)

.PHONY: all
all: dxf svg

.PHONY: dxf
dxf: $(DXFS)

.PHONY: svg
svg: $(SVGS)

.PHONY: clean
clean:
	-rm exploded.dxf

bottom.dxf: exploded.dxf
	$(FLATTEN) -o "$@" "$<" 'Case' 'Case lower' 'Bottom'

spacer.dxf: exploded.dxf
	$(FLATTEN) -o "$@" "$<" 'Case' 'Case lower' 'Spacer'

plate.dxf: exploded.dxf
	$(FLATTEN) -o "$@" "$<" 'Case' 'Case upper' 'Plate'

frame.dxf: exploded.dxf
	$(FLATTEN) -o "$@" "$<" 'Case' 'Case upper' 'Frame'

exploded.dxf: master.dxf
	$(EXPLODE) -o "$@" -r "$<"

$(SVGDIR):
	mkdir "$@"

$(SVGDIR)/%.svg: %.dxf | $(SVGDIR)
	$(TOSVG) -o "$@" "$<"