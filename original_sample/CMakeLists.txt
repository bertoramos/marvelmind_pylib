
# cmake_minimum_required(VERSION 3.15)
# project(marvelmind_pylib)
# find_package(Threads REQUIRED)
# add_executable(test_lib test_lib.cpp build/marvelmind.o)
# target_link_libraries(test_lib Threads::Threads)

cmake_minimum_required(VERSION 3.15)
project(original_sample)

find_package(Threads REQUIRED)
add_library(marvelmind.o OBJECT ../marvelmind.c)

add_executable(first_sample first_sample.cpp)
target_link_libraries(first_sample Threads::Threads marvelmind.o)
