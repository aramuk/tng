#!/pkg/python/3.6.8/bin/python3.6
from pathlib import Path
from .Image import Image

class DBItem:

    def __init__(self, path):
        loc = path
        if type(loc) is not Path:
            loc = Path(loc)
        if not loc.exists():
            raise ValueError(f'Can not find an image at {str(path)}')
        self.location = loc
    
    def _list_items(self, filetype=None, state=None,):
        fits = png = raw = ready = True
        if filetype is None:
            fits = png = True
        elif filetype not in ('png','fits'):
            exec(f'{filetype} = True')
        else:
            raise ValueError(f'filetype must be None, "png", or "fits".')
        if state is None:
            raw = ready = True
        elif state not in ('raw','ready'):
            exec(f'{state} = True')
        else:
            raise ValueError(f'state must be None, "raw", or "ready".')

        def _listgen():
            loc = self.location
            if fits:
                if raw:
                    for img in (loc / 'fits' / 'raw').iterdir():
                        yield Image(str(img))
                if ready:
                    for img in (loc / 'fits' / 'ready').iterdir():
                        yield Image(str(img))
            if png:
                if raw:
                    for img in (loc / 'png' / 'raw').iterdir():
                        yield Image(str(img))
                if ready:
                    for img in (loc / 'png' / 'ready').iterdir():
                        yield Image(str(img))
        return _listgen

    def __iter__(self):
        return self._list_items('ready')

    def raw(self, filetype=None):
        return self._list_items(filetype, 'raw')

    def ready(self, filetype=None):
        return self._list_items(filetype, 'ready')

    def fits(self, state=None):
        return self._list_items('fits', state)

    def png(self, state=None):
        return self._list_items('png', state)