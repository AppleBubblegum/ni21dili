import numpy as np
from ipywidgets import interact, fixed
from PIL import Image


def imshow(X, resize=None):
	img = Image.fromarray(X)
	img = img.resize(size=(resize[0], resize[1]))
	return img
