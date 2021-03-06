#!/usr/bin/env python
import os, os.path
from distutils.core import setup, Extension

source_files = ["Exception.cpp", "Context.cpp", "Engine.cpp", "Wrapper.cpp", "Debug.cpp", "PyV8.cpp"]

macros = [("BOOST_PYTHON_STATIC_LIB", None)]

include_dirs = [
  os.path.join(os.environ.get('V8_HOME'), 'include'),
]
library_dirs = []
libraries = []
extra_compile_args = []
extra_link_args = []
  
if os.name == "nt":
  include_dirs += [   
    os.environ.get('BOOST_HOME'),
    os.path.join(os.environ.get('PYTHON_HOME'), 'include'),
  ]
  library_dirs += [
    os.path.join(os.environ.get('V8_HOME'), 'tools\\visual_studio\\Release\\lib'),
    os.path.join(os.environ.get('BOOST_HOME'), 'stage/lib'),
    os.path.join(os.environ.get('PYTHON_HOME'), 'libs'),
  ]  
  
  include_dirs += [p for p in os.environ["INCLUDE"].split(';') if p]
  library_dirs += [p for p in os.environ["LIB"].split(';') if p]
  
  libraries += ["winmm", "ws2_32"]
  extra_compile_args += ["/O2", "/GL", "/MT", "/EHsc", "/Gy", "/Zi"]
  extra_link_args += ["/DLL", "/OPT:REF", "/OPT:ICF", "/MACHINE:X86"]
elif os.name == "posix":
  library_dirs += [
    os.environ.get('V8_HOME'),
  ]
  
  libraries = ["boost_python", "v8", "rt"]

pyv8 = Extension(name = "_PyV8",
                 sources = [os.path.join("src", file) for file in source_files],                 
                 define_macros = macros,
                 include_dirs = include_dirs,
                 library_dirs = library_dirs,
                 libraries = libraries,
                 extra_compile_args = extra_compile_args,
                 extra_link_args = extra_link_args,
                 )

setup(name='PyV8',
      version='0.7',
      description='Python Wrapper for Google V8 Engine',
      long_description="PyV8? is a python wrapper for Google V8 engine, it act as a bridge between the Python and JavaScript? objects, and support to hosting Google's v8 engine in a python script.",
      platforms="x86",
      author='Flier Lu',
      author_email='flier.lu@gmail.com',
      url='http://code.google.com/p/pyv8/',
      download_url='http://code.google.com/p/pyv8/downloads/list',
      license="Apache Software License",
      py_modules=['PyV8'],
      ext_modules=[pyv8],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX', 
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities', 
      ]
      )