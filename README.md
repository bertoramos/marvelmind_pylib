
# C Marvelmind API Binding

## Building

### Build marvelmind original sample

1. Create a build folder in original_sample folder
2. In build folder execute : cmake ..
3. In build folder execute : make

### Build marvelmind c++ test program (Unix)

1. Create a build folder in test_marvelmind_device folder
2. In build folder execute : cmake ..
3. In build folder execute : make

### Build marvelmind_pylib (Unix)

1. Create a python virtual environment and install pybind11
2. In marvelmind_pylib folder create a build folder
3. In build folder execute : cmake .. -Dpybind11_DIR=$(python -m pybind11 --cmakedir)
4. In build folder execute : make

### Build marvelmind_pylib (Windows)

1. Install Visual Studio.
2. Create a python virtual environment and install pybind11.
3. In marvelmind_pylib folder create a build folder.
4. In build folder execute : cmake ..
5. In build folder execute : cmake --build . --config Release --target marvelmind_pylib

## Install

### Install in python

1. Execute : python -m ensurepip
2. Execute : python -m pip install --upgrade pip
3. In marvelmind_pylib_setup execute : python -m pip install .


## Pre-build install

1. Execute ./python pip install https://github.com/bertoramos/marvelmind_pylib/releases/download/{version}/{so-version-file}.zip
