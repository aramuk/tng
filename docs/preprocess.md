# `tng.preprocess`

This module contains functions used for the parsing of retrieved FITS and PNG files from the TNG simulation.

## Function `extract_subhalo(data, outpath)`

Crops extraneous whitespace by isolating the subhalo using edge detection.

**Parameters:**
- **data**: a matrix of pixel data
- **outpath**: the filepath for the cropped image

## Function `extract_bands(inpath, outdir)`

Splits a .fits image into colorbands and saves them as separate .fits files.

**Parameters:**
- **inpath**: the path to the initial .fits image
- **outdir**: the directory to save the output images
