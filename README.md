[![Build Status](https://travis-ci.com/scivision/NCAR-GLOW.svg?branch=master)](https://travis-ci.com/scivision/NCAR-GLOW)

# GLOW
The GLobal airglOW Model

This directory contains:
   Fortran-90 source code files,
   Makefiles,
   Example input and output files,
   Example job script,
   Subdirectory data/ contains input data files,
   Subdirectory data/iri90 contains IRI input data files


### Build
You can call this repo from a Meson wrap or CMake Fetch.
To build by itself, do either:

```sh
cd build
cmake ..
cmake --build . -j
```

or 

```sh
cd build
meson ..
ninja
```
