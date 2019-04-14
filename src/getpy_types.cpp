#include "getpy.cpp"

#include <pybind11/pybind11.h>

using str16 = std::array<char, 16>;
using int32 = int32_t;
using uint32 = uint32_t;
using str1 = std::array<char, 1>;
using str2 = std::array<char, 2>;
using uint16 = uint16_t;
using uint8 = uint8_t;
using int8 = int8_t;
using str4 = std::array<char, 4>;
using int64 = int64_t;
using str32 = std::array<char, 32>;
using int16 = int16_t;
using float32 = float;
using uint64 = uint64_t;
using str8 = std::array<char, 8>;
using float64 = double;

PYBIND11_MODULE(_getpy, m) {
    m.doc() = "A Fast and Memory Efficient Hash Map for Python";

	declare_dict<str4, str1>(m, "Dict_str4_str1");
	declare_dict<str4, str2>(m, "Dict_str4_str2");
	declare_dict<str4, str4>(m, "Dict_str4_str4");
	declare_dict<str4, str8>(m, "Dict_str4_str8");
	declare_dict<str4, str16>(m, "Dict_str4_str16");
	declare_dict<str4, str32>(m, "Dict_str4_str32");
	declare_dict<str4, uint8>(m, "Dict_str4_uint8");
	declare_dict<str4, uint16>(m, "Dict_str4_uint16");
	declare_dict<str4, uint32>(m, "Dict_str4_uint32");
	declare_dict<str4, uint64>(m, "Dict_str4_uint64");
	declare_dict<str4, int8>(m, "Dict_str4_int8");
	declare_dict<str4, int16>(m, "Dict_str4_int16");
	declare_dict<str4, int32>(m, "Dict_str4_int32");
	declare_dict<str4, int64>(m, "Dict_str4_int64");
	declare_dict<str4, float32>(m, "Dict_str4_float32");
	declare_dict<str4, float64>(m, "Dict_str4_float64");
	declare_dict<str4, bool>(m, "Dict_str4_bool");
	declare_dict<str8, str1>(m, "Dict_str8_str1");
	declare_dict<str8, str2>(m, "Dict_str8_str2");
	declare_dict<str8, str4>(m, "Dict_str8_str4");
	declare_dict<str8, str8>(m, "Dict_str8_str8");
	declare_dict<str8, str16>(m, "Dict_str8_str16");
	declare_dict<str8, str32>(m, "Dict_str8_str32");
	declare_dict<str8, uint8>(m, "Dict_str8_uint8");
	declare_dict<str8, uint16>(m, "Dict_str8_uint16");
	declare_dict<str8, uint32>(m, "Dict_str8_uint32");
	declare_dict<str8, uint64>(m, "Dict_str8_uint64");
	declare_dict<str8, int8>(m, "Dict_str8_int8");
	declare_dict<str8, int16>(m, "Dict_str8_int16");
	declare_dict<str8, int32>(m, "Dict_str8_int32");
	declare_dict<str8, int64>(m, "Dict_str8_int64");
	declare_dict<str8, float32>(m, "Dict_str8_float32");
	declare_dict<str8, float64>(m, "Dict_str8_float64");
	declare_dict<str8, bool>(m, "Dict_str8_bool");
	declare_dict<uint32, str1>(m, "Dict_uint32_str1");
	declare_dict<uint32, str2>(m, "Dict_uint32_str2");
	declare_dict<uint32, str4>(m, "Dict_uint32_str4");
	declare_dict<uint32, str8>(m, "Dict_uint32_str8");
	declare_dict<uint32, str16>(m, "Dict_uint32_str16");
	declare_dict<uint32, str32>(m, "Dict_uint32_str32");
	declare_dict<uint32, uint8>(m, "Dict_uint32_uint8");
	declare_dict<uint32, uint16>(m, "Dict_uint32_uint16");
	declare_dict<uint32, uint32>(m, "Dict_uint32_uint32");
	declare_dict<uint32, uint64>(m, "Dict_uint32_uint64");
	declare_dict<uint32, int8>(m, "Dict_uint32_int8");
	declare_dict<uint32, int16>(m, "Dict_uint32_int16");
	declare_dict<uint32, int32>(m, "Dict_uint32_int32");
	declare_dict<uint32, int64>(m, "Dict_uint32_int64");
	declare_dict<uint32, float32>(m, "Dict_uint32_float32");
	declare_dict<uint32, float64>(m, "Dict_uint32_float64");
	declare_dict<uint32, bool>(m, "Dict_uint32_bool");
	declare_dict<uint64, str1>(m, "Dict_uint64_str1");
	declare_dict<uint64, str2>(m, "Dict_uint64_str2");
	declare_dict<uint64, str4>(m, "Dict_uint64_str4");
	declare_dict<uint64, str8>(m, "Dict_uint64_str8");
	declare_dict<uint64, str16>(m, "Dict_uint64_str16");
	declare_dict<uint64, str32>(m, "Dict_uint64_str32");
	declare_dict<uint64, uint8>(m, "Dict_uint64_uint8");
	declare_dict<uint64, uint16>(m, "Dict_uint64_uint16");
	declare_dict<uint64, uint32>(m, "Dict_uint64_uint32");
	declare_dict<uint64, uint64>(m, "Dict_uint64_uint64");
	declare_dict<uint64, int8>(m, "Dict_uint64_int8");
	declare_dict<uint64, int16>(m, "Dict_uint64_int16");
	declare_dict<uint64, int32>(m, "Dict_uint64_int32");
	declare_dict<uint64, int64>(m, "Dict_uint64_int64");
	declare_dict<uint64, float32>(m, "Dict_uint64_float32");
	declare_dict<uint64, float64>(m, "Dict_uint64_float64");
	declare_dict<uint64, bool>(m, "Dict_uint64_bool");
	declare_dict<int32, str1>(m, "Dict_int32_str1");
	declare_dict<int32, str2>(m, "Dict_int32_str2");
	declare_dict<int32, str4>(m, "Dict_int32_str4");
	declare_dict<int32, str8>(m, "Dict_int32_str8");
	declare_dict<int32, str16>(m, "Dict_int32_str16");
	declare_dict<int32, str32>(m, "Dict_int32_str32");
	declare_dict<int32, uint8>(m, "Dict_int32_uint8");
	declare_dict<int32, uint16>(m, "Dict_int32_uint16");
	declare_dict<int32, uint32>(m, "Dict_int32_uint32");
	declare_dict<int32, uint64>(m, "Dict_int32_uint64");
	declare_dict<int32, int8>(m, "Dict_int32_int8");
	declare_dict<int32, int16>(m, "Dict_int32_int16");
	declare_dict<int32, int32>(m, "Dict_int32_int32");
	declare_dict<int32, int64>(m, "Dict_int32_int64");
	declare_dict<int32, float32>(m, "Dict_int32_float32");
	declare_dict<int32, float64>(m, "Dict_int32_float64");
	declare_dict<int32, bool>(m, "Dict_int32_bool");
	declare_dict<int64, str1>(m, "Dict_int64_str1");
	declare_dict<int64, str2>(m, "Dict_int64_str2");
	declare_dict<int64, str4>(m, "Dict_int64_str4");
	declare_dict<int64, str8>(m, "Dict_int64_str8");
	declare_dict<int64, str16>(m, "Dict_int64_str16");
	declare_dict<int64, str32>(m, "Dict_int64_str32");
	declare_dict<int64, uint8>(m, "Dict_int64_uint8");
	declare_dict<int64, uint16>(m, "Dict_int64_uint16");
	declare_dict<int64, uint32>(m, "Dict_int64_uint32");
	declare_dict<int64, uint64>(m, "Dict_int64_uint64");
	declare_dict<int64, int8>(m, "Dict_int64_int8");
	declare_dict<int64, int16>(m, "Dict_int64_int16");
	declare_dict<int64, int32>(m, "Dict_int64_int32");
	declare_dict<int64, int64>(m, "Dict_int64_int64");
	declare_dict<int64, float32>(m, "Dict_int64_float32");
	declare_dict<int64, float64>(m, "Dict_int64_float64");
	declare_dict<int64, bool>(m, "Dict_int64_bool");
}