#!/bin/bash

# Sets pybind11 cmake directory
pybind11_DIR=$(python -m pybind11 --cmakedir)

# Creates build directory
mkdir -p ./makefiles/unix_build
cd ./makefiles/unix_build

# Builds
cmake .. -Dpybind11_DIR=$(python3 -m pybind11 --cmakedir)
make

# Returns to the root directory
cd ../../
