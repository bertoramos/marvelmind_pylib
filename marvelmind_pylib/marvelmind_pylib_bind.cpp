
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "../marvelmind_device.hpp"

namespace py = pybind11;

PYBIND11_MODULE(marvelmind_pylib, m) {
    m.doc() = "MarvelMindDevice class";

    py::class_<MarvelMindDevice>(m, "MarvelMindDevice")
        .def(py::init<string, bool>())
        .def("start", &MarvelMindDevice::start)
        .def("close", &MarvelMindDevice::close)
        .def("getMobileBeaconsPosition", &MarvelMindDevice::getMobileBeaconsPosition)
        .def("getStationaryBeaconsPosition", &MarvelMindDevice::getStationaryBeaconsPosition);

};
