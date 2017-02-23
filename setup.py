#!/usr/bin/env python
import setuptools #enables develop
from numpy.distutils.core import setup,Extension
from glob import glob
from os.path import join

req = ['nose','numpy','pandas','matplotlib']

#%% fortran data files
iridata = glob(join('data','*.asc'))
#%% install
setup(name='pyiri90',
      packages=['pyiri90'],
      author='Michael Hirsch, Ph.D.',
      ext_modules=[Extension(name='iri90',
                    sources=['fortran/iri90.f'],
                    f2py_options=['--quiet'])],
     data_files=[('pyiri90/data',iridata)],
     install_requires=req,
	  )
