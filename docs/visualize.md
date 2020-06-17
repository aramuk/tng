# `tng.visualize`

This module contains helped functions for easily visualize large portions of collected data.

## Function `plot_grid(items, func, dim, fig_args, plt_args)`

Plots a list of images in a grid.

**Parameters:**
- **items**: a sequence of image objects to plot
- **func**: a plot function that takes an `Axis` as its first parameter, image as its second, and any number of `matplotlib.pyplot` arguments
- **dim**: the width of the figure (in plots)
- **fig_args**: key-word arguments to `matplotlib.pyplot.subplots`
- **plt_args**: key-word arguments to `matplotlib.pyplot.plot`

**Returns:** a `matplotlib.pyplot.Figure` and its `Axes`

## Function `plot_imgs(images, dim, fig_args, plt_args)`

Creates a grid using `matplotlib.pyplot.imshow` as a plot function.

**Parameters:**
- **images**: a sequence of image objects to plot
- **dim**: the width of the figure (in plots)
- **fig_args**: key-word arguments to `matplotlib.pyplot.subplots`
- **plt_args**: key-word arguments to `matplotlib.pyplot.plot`

**Returns:** a `matplotlib.pyplot.Figure` and its `Axes`

**Parameters:**
- **inpath**: the path to the initial .fits image
- **outdir**: the directory to save the output images

## Function `plot_mats(matrices, dim, fig_args, plt_args)`

Creates a grid using `matplotlib.pyplot.matshow` as a plot function.

**Parameters:**
- **images**: a sequence of image objects to plot
- **dim**: the width of the figure (in plots)
- **fig_args**: key-word arguments to `matplotlib.pyplot.subplots`
- **plt_args**: key-word arguments to `matplotlib.pyplot.plot`

**Returns:** a `matplotlib.pyplot.Figure` and its `Axes`

## `plot_sequence(I: np.ndarray, ax: plt.Axes, funcs: list, **kwargs)`

Plots a single image using a sequence of transformation functions

**Parameters:**
- **I**: image data represented as a matrix
- **ax**: the axis of a figure along which to plot the sequence
- **funcs**: a list of functions that take a single matrix as a parameter and transform it
- **kwargs**: key-word arguments to `matplotlib.pyplot.imshow`
