
# cmake_minimum_required(VERSION 3.15)
# project(marvelmind_pylib)
# find_package(Threads REQUIRED)
# add_executable(test_lib test_lib.cpp build/marvelmind.o)
# target_link_libraries(test_lib Threads::Threads)

cmake_minimum_required(VERSION 3.15)
project(marvelmind_device_test)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_library(marvelmind.o OBJECT ../marvelmind.c)

find_package(Threads REQUIRED)
add_executable(test_lib test_lib.cpp)
target_link_libraries(test_lib Threads::Threads marvelmind.o)
