import sys
import importlib

class ExcBCH(Exception):
    pass

class BCHCLASS:
    @property
    def fpath(self):
        return self._fpath
    @fpath.setter
    def fpath(self,val ):
        if hasattr(self, '_fpath'):
            raise ExcBCH( '\n\tCANNOT RESET FILE' )
        self._fpath = val
    @property
    def bname(self):
        return bname4fpath(self.fpath)

    @property
    def fname(self):
        return fname4fpath(self.fpath)


try:              __builtins__['BCH']
except KeyError:  __builtins__['BCH'] = BCHCLASS()
BCH=__builtins__['BCH']

def split_path(fpath):#, bases=sys.path):
    for bpath in sys.path:
        if not bpath.endswith('/'):
            bpath = bpath + '/'
        if fpath.startswith(bpath):
            return bpath, fpath[len(bpath):]
    return '',''

def fname4fpath(fpath):
    assert fpath.endswith('.py')
    bpath, rpath = split_path(fpath[:-3])
    if rpath:
        return rpath.replace('/','.')

def bname4fpath(fpath):
    parts=fname4fpath(fpath).split('.')
    return '.'.join(parts[:3])

def dnames4__file__(file):
    class Namespace: pass
    ret=Namespace()
    ret.base=bname4fpath(file)
    ret.full=fname4fpath(file)
    lbin.bch.DNAMES=ret
    return ret



