#!/usr/bin/python3

import base64
from subprocess import run
from os import listdir
from os.path import normpath, join, isfile, splitext

ASSETS_DIR=normpath("./style_src/assets/")
ASSETS_SCSS=normpath("./style_src/_assets.scss")
USERSTYLE_SCSS=normpath("./style_src/pinkseamobile.scss")
USERSTYLE_CSS=normpath("./pinkseamobile.user.styl")

# Assets stored in filename:dataURL pairs
assets = {}

print("Scanning for assets...")

# Populate the dict with asset filenames
for filename in listdir(ASSETS_DIR):
	filepath = join(ASSETS_DIR, filename)
	
	if isfile(filepath):
		assets[filename] = ""
		
		print(f"* Asset {filename} has been found.")
print(f"{len(assets)} assets have been found.")
print("Encoding assets...")

# Populate the dict with dataURLs
for filename in assets.keys():
	filepath = join(ASSETS_DIR, filename)

	with open(filepath, mode="rb") as f:
		content = f.read()
		encoded = base64.b64encode(content).decode("ascii")
		
		assets[filename] = encoded
		
		print(f"* Asset {filename} has been encoded.")
print("Generating _assets.scss...")

# Generate _assets.scss
if len(assets)>0:
	content = ""

	for filename in assets.keys():
		name = splitext(filename)[0]
	
		content += f"$asset-{name}: url(\"data:image/png;base64,{assets[filename]}\");\n"
	
	with open(ASSETS_SCSS, mode="w", encoding="utf-8") as f:
		f.write(content)
print("Done!")
print("Compiling final stylesheet...")

run(["sass", "--style=compact", "--sourcemap=none", USERSTYLE_SCSS, USERSTYLE_CSS])

print(f"Stylesheet successfully compiled at ./{USERSTYLE_CSS}!")
