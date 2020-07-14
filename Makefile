.DEFAULT_GOAL: all
.PHONY: all

all:
	./Folders.py

save_screenshot.png:
	./save-screenshot.py https://www.yahoo.co.jp/ $@

body.png:
	./body.py https://www.yahoo.co.jp/ $@

selector.png:
	./selector.py https://www.tenki.jp/ $@ "div#forecast-map-wrap"

