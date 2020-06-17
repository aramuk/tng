#!/pkg/python/3.6.8/bin/python3.6
from math import ceil
import numpy as np
import matplotlib.pyplot as plt

def plot_grid(items, func, dim, fig_args, plt_args):
	fig, ax = plt.subplots(ceil(len(items)/dim), dim, **fig_args)
	axf = ax.flatten()
	for i,I in enumerate(items):
		func(axf[i], I, **plt_args)
	return fig, ax

def plot_imgs(images, dim, fig_args, plt_args):
	def imshow(axis, image, **kwargs):
		axis.imshow(image, **kwargs)
	return plot_grid(images, imshow, dim, fig_args, plt_args)
	

def plot_mats(matrices, dim, fig_args, plt_args):
	def matshow(axis, mat, **kwargs):
		axis.matshow(mat, **kwargs)
	return plot_grid(matrices, matshow, dim, fig_args, plt_args)

def plot_sequence(I: np.ndarray, ax: plt.Axes, funcs: list, **kwargs):
	if len(funcs) != len(ax)-1:
		raise ValueError(f'Received {len(funcs)} functions; expected {len(ax)}')
	visualizations = [lambda X:X] + funcs
	axf = ax.flatten()
	for i,vis in enumerate(visualizations):
		axf[i].imshow(vis(I), **kwargs)
