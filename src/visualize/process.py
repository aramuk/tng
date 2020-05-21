#!/bin/python3.6

from math import ceil
import numpy as np
import matplotlib.pyplot as plt

def plot_imgs(images, **kwargs):
	fig, ax = plt.subplots(4, ceil(len(images)/4))	
	axf = axf.flatten()
	for i,I in enumerate(images):
		axf[i].imshow(I, **kwargs)
	return fig, ax	

def plot_sequence(I: np.ndarray, ax: plt.Axis, funcs: list, **kwargs):
	if len(funcs) != len(ax)-1:
		raise ValueError(f'Received {len(funcs)} functions; expected {len(ax}')
	visualizations = [lambda X:X] + funcs
	axf = ax.flatten()
	for i,vis in enumerate(visualizations):
		axf[i].imshow(vis(I), **kwargs)
