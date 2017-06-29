# IMG #
Image Manipulation Genie

### Travis CI (Current Build) [![Build Status](https://travis-ci.org/CnuUasLab/IMG.svg?branch=develop)](https://travis-ci.org/CnuUasLab/IMG)

### How to Run: ###
```
git clone https://github.com/CnuUasLab/IMG.git
cd IMG
pip install -r Requirements.txt
sudo apt-get install python-imaging-tk
python img.py
```

Notes:
Use python -m pip install... on certain system setups.
Also, ensure python is in your evironment path.

### Keyboard Cmds: ###
```
O   goto Original image list
P   goto Processed image list

N   Previous image
M   Next image

D   Deletes current image in crop list

C   Crop regions of interests (red boxes)
R   Reset ROIs
L   List ROI points (for debugging)

X   Saves json file and image for current image

A   Opens window to select alternate directory
```
