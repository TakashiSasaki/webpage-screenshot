.DEFAULT_GOAL: all
.PHONY: all

all: save_screenshot.png body.png

save_screenshot.png:
	./save-screenshot.py https://www.yahoo.co.jp/ $@

body.png:
	./body.py https://www.yahoo.co.jp/ $@

