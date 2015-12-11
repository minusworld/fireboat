from SimpleCV import *
import os
import datetime

# width and height of images from FLIR
global_w = 80
global_h = 60

# how many segments to divde the image into
# along each axis. total number of image
# segments will be this number, squared (x^2):
#  1  2  3
# ---------
# |  |  |  | 1
# ---------
# |  |  |  | 2
# ---------
# |  |  |  | 3
# ---------
segments = 3

FILTER_THRESHOLD = sum( (Image((global_w/segments, global_h/segments).invert()) / 13).getNumpy().flatten() )

# helper method for showing an image.
def show_image(img):
    win=img.show()
    raw_input()
    win.quit()

#### Scoring mechanism:
# Find the distance between the image and the color Yellow,
# resulting in black wherever yellow exists in the original
# image.  This means that a segment with the "lowest" color
# value in the yellow distance image (again, yellow becomes
# black in the distance image) is the segment which has the
# most yellow.
def yellow_score(img):
    yellow_distance = img.colorDistance(Color.YELLOW)
    return sum(yellow_distance.getNumpy().flatten())

def score(img):
    return yellow_score(img)  # just does yellow_score for now, may change

def score_alt(img):
    score = sum(img.getNumpy().flatten())
    print img.getNumpy()
    return score

# scores each grid
# returns the grid index of the winning grid
# and the score.
def score_grids(img):
    grids = gridify(img)
    min_score = 0xffffffff
    grid_index = -1
    for i, grid in enumerate(grids):
        this_score = score(grid)
        if this_score < min_score:
            min_score = this_score
            grid_index = i
    return (grid_index, min_score)

def score_grids_max(img):
    grids = gridify(img)
    max_score = 0
    grid_index = -1
    for i, grid in enumerate(grids):
        this_score = score_alt(grid)
        if this_score > max_score and filter_img(grid, this_score, FILTER_THRESHOLD):
            max_score = this_score
            grid_index = i
    return (grid_index, max_score)

def filter_img(img, score, score_threshold):
    if score(img) < score_threshold:
        return False
    else:
        return True

# divides an image into equally-sized regions 
# grids returned like so, for s=3:
# [ [0] [1] [2]
#   [3] [4] [5]
#   [6] [7] [8] ]
def gridify(img, s=3):
    grids = []
    w = 0
    h = 0
    w_delta = img.width / s
    h_delta = img.height / s
    w_part = img.width % s
    h_part = img.height % s
    for i in range(s):
        for j in range(s):
            grids.append(img.crop(w, h, w_delta, h_delta))
            w += w_delta
            if w >= img.width-w_part:
                w = 0
        h += h_delta
        if  h >= img.height-h_part:
            h = 0
    return grids

# returns a tuple with the grid index and
# the grid's score:  (index, score)
def target(img, show=False):
    grids = gridify(img)
    #score = score_grids(img)
    score = score_grids_max(img)
    if show:
        win = grids[score[0]].show()
    return score

def fire_in_view(score):
    if score[0] == 5:
        return True
    else:
        return False

def target_from_file(filename):
    if os.path.isfile(filename):
        img = Image(filename)
        score = target(img, True)
        #os.remove(filename)
	os.rename(filename, filename + str(datetime.datetime.now()) + ".png")
        return score
    else:
        raise FileNotFoundError
