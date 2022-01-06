import numpy as np
from PIL import Image, ImageFont, ImageDraw
from PIL.ImageChops import add, subtract, multiply, difference, screen
import PIL.ImageStat as Stat
from skimage.io import imread, imsave, imshow, show, imread_collection, imshow_collection
from skimage import color, viewer, exposure, img_as_float, data
from skimage.transform import SimilarityTransform, warp, swirl
from skimage.util import invert, random_noise, montage
import matplotlib.image as mping
import matplotlib.pylab as plt
from scipy.ndimage import affine_transform, zoom
import imageio


class Process:
    def __init__(self, org, mod):
        self.o = org
        self.m = mod
    def binaryzation(self):

