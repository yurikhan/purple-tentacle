SVGS = $(wildcard ../docs/content/images/05-electrical-design/*.svg)

.PHONY: crop
crop:
	$(foreach i,$(SVGS), \
		inkscape \
			--verb=FitCanvasToDrawing \
			--verb=FileSave \
			--verb=FileQuit $(i);)
