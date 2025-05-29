@ECHO OFF

rem Sets pybind11 cmake directory
for /F %%i in ('python -m pybind11 --cmakedir') do set pybind11_DIR=%%i

rem Creates build directory
mkdir .\marvelmind_pylib\win_build
cd .\marvelmind_pylib\win_build

rem Builds
cmake ..
cmake --build . --config Release --target marvelmind_pylib
cd ..\..\
