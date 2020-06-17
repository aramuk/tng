#!/pkg/python/3.6.8/bin/python3.6
from astropy.io import fits
from pathlib import Path

def extract_colorbands(inpath, outdir):
    # Bands to extract
	COLORBANDS = ('Gband','Rband','Iband','Zband')

	# Read FITS file
	primaryHDU = fits.getdata(inpath, ext=0)

	# Iterate over the bands in the FITS file and save them to the output directory
	for band, name in zip(primaryHDU, COLORBANDS):
		outpath = outdir / (inpath.stem + '_' + name + '.fits')
		hdu = fits.PrimaryHDU(band)
        hdul = fits.HDUList([hdu])
        hdul.writeto(outpath)
