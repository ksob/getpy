#include "getpy.cpp"

#include <pybind11/pybind11.h>


PYBIND11_MODULE(_getpy, m) {
    m.doc() = "A Fast and Memory Efficient Hash Map for Python";


    declare_dict<uint64_t, uint8_t>(m, "Dict_uint64_uint8");

}
