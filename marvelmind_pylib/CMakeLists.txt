
# cmake_minimum_required(VERSION 3.15)
# project(marvelmind_pylib)
# find_package(Threads REQUIRED)
# add_executable(test_lib test_lib.cpp build/marvelmind.o)
# target_link_libraries(test_lib Threads::Threads)

cmake_minimum_required(VERSION 3.15)
project(marvelmind_device_test)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

find_package(pybind11 REQUIRED)
find_package(Threads REQUIRED)
pybind11_add_module(marvelmind_pylib marvelmind_pylib_bind.cpp ../marvelmind_device.hpp ../marvelmind.c ../marvelmind.h)
target_link_libraries(marvelmind_pylib PRIVATE Threads::Threads)
