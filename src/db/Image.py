from pathlib import Path
import matplotlib.pyplot as plt
from astropy.io import fits

class Image:

    def __init__(self, path):
        loc = path
        if type(loc) is not Path:
            loc = Path(loc)
        if not loc.exists():
            raise ValueError(f'Can not find an image at {str(path)}')
        self.location = loc
        if 'fits' in loc.suffixes:
            self.type = 'fits'
        elif 'png' in loc.suffixes:
            self.type = 'png'
        else:
            raise ValueError(f'Can only load PNG and FITS images')
    
    def _read_as_fits(self):
        return fits.getdata(str(self.location), ext=0)

    def _read_as_png(self):
        return plt.imread(str(self.location))

    def get_data(self):
        return self._read_as_fits() if self.type == 'fits' else self._read_as_png()

    def show(self, *args, **kwargs):
        data = self.get_data()
        if self.type == 'fits':
            nBands,m,n = data.shape
            fig,ax = plt.subplots(1,nBands, figsize=(15,10))
            for i,img in enumerate(data):
                ax[i].imshow(img, *args, **kwargs)
                ax[i].set_xlabel('Band {}'.format(i))
            return fig,ax
        else:
            fig,ax = plt.subplots(1,1,figsize=(10,10))
            ax.imshow(data, *args, **kwargs)
            return fig,ax
        
        


