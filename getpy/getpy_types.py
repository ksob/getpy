import numpy as np

import _getpy as _gp

types = {
    'str4' : np.dtype('U4'),
    'str8' : np.dtype('U8'),
    'str16' : np.dtype('U16'),
    'str32' : np.dtype('U32'),
    'uint8' : np.dtype('u1'),
    'uint16' : np.dtype('u2'),
    'uint32' : np.dtype('u4'),
    'uint64' : np.dtype('u8'),
    'int8' : np.dtype('i1'),
    'int16' : np.dtype('i2'),
    'int32' : np.dtype('i4'),
    'int64' : np.dtype('i8'),
    'float32' : np.dtype('f4'),
    'float64' : np.dtype('f8'),
    'pair_str4_str4' : np.dtype({'names': ['first', 'second'], 'formats': ['U4', 'U4']}),
    'pair_str8_str8' : np.dtype({'names': ['first', 'second'], 'formats': ['U8', 'U8']}),
    'pair_str16_str16' : np.dtype({'names': ['first', 'second'], 'formats': ['U16', 'U16']}),
    'pair_str32_str32' : np.dtype({'names': ['first', 'second'], 'formats': ['U32', 'U32']}),
    'pair_uint8_uint8' : np.dtype({'names': ['first', 'second'], 'formats': ['u1', 'u1']}),
    'pair_uint16_uint16' : np.dtype({'names': ['first', 'second'], 'formats': ['u2', 'u2']}),
    'pair_uint32_uint32' : np.dtype({'names': ['first', 'second'], 'formats': ['u4', 'u4']}),
    'pair_uint64_uint64' : np.dtype({'names': ['first', 'second'], 'formats': ['u8', 'u8']}),
    'pair_int8_int8' : np.dtype({'names': ['first', 'second'], 'formats': ['i1', 'i1']}),
    'pair_int16_int16' : np.dtype({'names': ['first', 'second'], 'formats': ['i2', 'i2']}),
    'pair_int32_int32' : np.dtype({'names': ['first', 'second'], 'formats': ['i4', 'i4']}),
    'pair_int64_int64' : np.dtype({'names': ['first', 'second'], 'formats': ['i8', 'i8']}),
    'pair_float32_float32' : np.dtype({'names': ['first', 'second'], 'formats': ['f4', 'f4']}),
    'pair_float64_float64' : np.dtype({'names': ['first', 'second'], 'formats': ['f8', 'f8']}),
    'bytearray2' : np.dtype({'names': ['bytearray'], 'formats': ['2u1']}),
    'bytearray4' : np.dtype({'names': ['bytearray'], 'formats': ['4u1']}),
    'bytearray8' : np.dtype({'names': ['bytearray'], 'formats': ['8u1']}),
    'bytearray10' : np.dtype({'names': ['bytearray'], 'formats': ['10u1']}),
    'bytearray16' : np.dtype({'names': ['bytearray'], 'formats': ['16u1']}),
    'bytearray20' : np.dtype({'names': ['bytearray'], 'formats': ['20u1']}),
    'bytearray30' : np.dtype({'names': ['bytearray'], 'formats': ['30u1']}),
    'bytearray32' : np.dtype({'names': ['bytearray'], 'formats': ['32u1']}),
    'bytearray40' : np.dtype({'names': ['bytearray'], 'formats': ['40u1']}),
    'bytearray50' : np.dtype({'names': ['bytearray'], 'formats': ['50u1']}),
}

dict_types = {
    (types['str4'], types['str4']) : _gp.Dict_str4_str4,
    (types['str4'], types['str8']) : _gp.Dict_str4_str8,
    (types['str4'], types['str16']) : _gp.Dict_str4_str16,
    (types['str4'], types['str32']) : _gp.Dict_str4_str32,
    (types['str4'], types['uint8']) : _gp.Dict_str4_uint8,
    (types['str4'], types['uint16']) : _gp.Dict_str4_uint16,
    (types['str4'], types['uint32']) : _gp.Dict_str4_uint32,
    (types['str4'], types['uint64']) : _gp.Dict_str4_uint64,
    (types['str4'], types['int8']) : _gp.Dict_str4_int8,
    (types['str4'], types['int16']) : _gp.Dict_str4_int16,
    (types['str4'], types['int32']) : _gp.Dict_str4_int32,
    (types['str4'], types['int64']) : _gp.Dict_str4_int64,
    (types['str4'], types['float32']) : _gp.Dict_str4_float32,
    (types['str4'], types['float64']) : _gp.Dict_str4_float64,
    (types['str4'], types['pair_str4_str4']) : _gp.Dict_str4_pair_str4_str4,
    (types['str4'], types['pair_str8_str8']) : _gp.Dict_str4_pair_str8_str8,
    (types['str4'], types['pair_str16_str16']) : _gp.Dict_str4_pair_str16_str16,
    (types['str4'], types['pair_str32_str32']) : _gp.Dict_str4_pair_str32_str32,
    (types['str4'], types['pair_uint8_uint8']) : _gp.Dict_str4_pair_uint8_uint8,
    (types['str4'], types['pair_uint16_uint16']) : _gp.Dict_str4_pair_uint16_uint16,
    (types['str4'], types['pair_uint32_uint32']) : _gp.Dict_str4_pair_uint32_uint32,
    (types['str4'], types['pair_uint64_uint64']) : _gp.Dict_str4_pair_uint64_uint64,
    (types['str4'], types['pair_int8_int8']) : _gp.Dict_str4_pair_int8_int8,
    (types['str4'], types['pair_int16_int16']) : _gp.Dict_str4_pair_int16_int16,
    (types['str4'], types['pair_int32_int32']) : _gp.Dict_str4_pair_int32_int32,
    (types['str4'], types['pair_int64_int64']) : _gp.Dict_str4_pair_int64_int64,
    (types['str4'], types['pair_float32_float32']) : _gp.Dict_str4_pair_float32_float32,
    (types['str4'], types['pair_float64_float64']) : _gp.Dict_str4_pair_float64_float64,
    (types['str4'], types['bytearray2']) : _gp.Dict_str4_bytearray2,
    (types['str4'], types['bytearray4']) : _gp.Dict_str4_bytearray4,
    (types['str4'], types['bytearray8']) : _gp.Dict_str4_bytearray8,
    (types['str4'], types['bytearray10']) : _gp.Dict_str4_bytearray10,
    (types['str4'], types['bytearray16']) : _gp.Dict_str4_bytearray16,
    (types['str4'], types['bytearray20']) : _gp.Dict_str4_bytearray20,
    (types['str4'], types['bytearray30']) : _gp.Dict_str4_bytearray30,
    (types['str4'], types['bytearray32']) : _gp.Dict_str4_bytearray32,
    (types['str4'], types['bytearray40']) : _gp.Dict_str4_bytearray40,
    (types['str4'], types['bytearray50']) : _gp.Dict_str4_bytearray50,
    (types['str8'], types['str4']) : _gp.Dict_str8_str4,
    (types['str8'], types['str8']) : _gp.Dict_str8_str8,
    (types['str8'], types['str16']) : _gp.Dict_str8_str16,
    (types['str8'], types['str32']) : _gp.Dict_str8_str32,
    (types['str8'], types['uint8']) : _gp.Dict_str8_uint8,
    (types['str8'], types['uint16']) : _gp.Dict_str8_uint16,
    (types['str8'], types['uint32']) : _gp.Dict_str8_uint32,
    (types['str8'], types['uint64']) : _gp.Dict_str8_uint64,
    (types['str8'], types['int8']) : _gp.Dict_str8_int8,
    (types['str8'], types['int16']) : _gp.Dict_str8_int16,
    (types['str8'], types['int32']) : _gp.Dict_str8_int32,
    (types['str8'], types['int64']) : _gp.Dict_str8_int64,
    (types['str8'], types['float32']) : _gp.Dict_str8_float32,
    (types['str8'], types['float64']) : _gp.Dict_str8_float64,
    (types['str8'], types['pair_str4_str4']) : _gp.Dict_str8_pair_str4_str4,
    (types['str8'], types['pair_str8_str8']) : _gp.Dict_str8_pair_str8_str8,
    (types['str8'], types['pair_str16_str16']) : _gp.Dict_str8_pair_str16_str16,
    (types['str8'], types['pair_str32_str32']) : _gp.Dict_str8_pair_str32_str32,
    (types['str8'], types['pair_uint8_uint8']) : _gp.Dict_str8_pair_uint8_uint8,
    (types['str8'], types['pair_uint16_uint16']) : _gp.Dict_str8_pair_uint16_uint16,
    (types['str8'], types['pair_uint32_uint32']) : _gp.Dict_str8_pair_uint32_uint32,
    (types['str8'], types['pair_uint64_uint64']) : _gp.Dict_str8_pair_uint64_uint64,
    (types['str8'], types['pair_int8_int8']) : _gp.Dict_str8_pair_int8_int8,
    (types['str8'], types['pair_int16_int16']) : _gp.Dict_str8_pair_int16_int16,
    (types['str8'], types['pair_int32_int32']) : _gp.Dict_str8_pair_int32_int32,
    (types['str8'], types['pair_int64_int64']) : _gp.Dict_str8_pair_int64_int64,
    (types['str8'], types['pair_float32_float32']) : _gp.Dict_str8_pair_float32_float32,
    (types['str8'], types['pair_float64_float64']) : _gp.Dict_str8_pair_float64_float64,
    (types['str8'], types['bytearray2']) : _gp.Dict_str8_bytearray2,
    (types['str8'], types['bytearray4']) : _gp.Dict_str8_bytearray4,
    (types['str8'], types['bytearray8']) : _gp.Dict_str8_bytearray8,
    (types['str8'], types['bytearray10']) : _gp.Dict_str8_bytearray10,
    (types['str8'], types['bytearray16']) : _gp.Dict_str8_bytearray16,
    (types['str8'], types['bytearray20']) : _gp.Dict_str8_bytearray20,
    (types['str8'], types['bytearray30']) : _gp.Dict_str8_bytearray30,
    (types['str8'], types['bytearray32']) : _gp.Dict_str8_bytearray32,
    (types['str8'], types['bytearray40']) : _gp.Dict_str8_bytearray40,
    (types['str8'], types['bytearray50']) : _gp.Dict_str8_bytearray50,
    (types['uint32'], types['str4']) : _gp.Dict_uint32_str4,
    (types['uint32'], types['str8']) : _gp.Dict_uint32_str8,
    (types['uint32'], types['str16']) : _gp.Dict_uint32_str16,
    (types['uint32'], types['str32']) : _gp.Dict_uint32_str32,
    (types['uint32'], types['uint8']) : _gp.Dict_uint32_uint8,
    (types['uint32'], types['uint16']) : _gp.Dict_uint32_uint16,
    (types['uint32'], types['uint32']) : _gp.Dict_uint32_uint32,
    (types['uint32'], types['uint64']) : _gp.Dict_uint32_uint64,
    (types['uint32'], types['int8']) : _gp.Dict_uint32_int8,
    (types['uint32'], types['int16']) : _gp.Dict_uint32_int16,
    (types['uint32'], types['int32']) : _gp.Dict_uint32_int32,
    (types['uint32'], types['int64']) : _gp.Dict_uint32_int64,
    (types['uint32'], types['float32']) : _gp.Dict_uint32_float32,
    (types['uint32'], types['float64']) : _gp.Dict_uint32_float64,
    (types['uint32'], types['pair_str4_str4']) : _gp.Dict_uint32_pair_str4_str4,
    (types['uint32'], types['pair_str8_str8']) : _gp.Dict_uint32_pair_str8_str8,
    (types['uint32'], types['pair_str16_str16']) : _gp.Dict_uint32_pair_str16_str16,
    (types['uint32'], types['pair_str32_str32']) : _gp.Dict_uint32_pair_str32_str32,
    (types['uint32'], types['pair_uint8_uint8']) : _gp.Dict_uint32_pair_uint8_uint8,
    (types['uint32'], types['pair_uint16_uint16']) : _gp.Dict_uint32_pair_uint16_uint16,
    (types['uint32'], types['pair_uint32_uint32']) : _gp.Dict_uint32_pair_uint32_uint32,
    (types['uint32'], types['pair_uint64_uint64']) : _gp.Dict_uint32_pair_uint64_uint64,
    (types['uint32'], types['pair_int8_int8']) : _gp.Dict_uint32_pair_int8_int8,
    (types['uint32'], types['pair_int16_int16']) : _gp.Dict_uint32_pair_int16_int16,
    (types['uint32'], types['pair_int32_int32']) : _gp.Dict_uint32_pair_int32_int32,
    (types['uint32'], types['pair_int64_int64']) : _gp.Dict_uint32_pair_int64_int64,
    (types['uint32'], types['pair_float32_float32']) : _gp.Dict_uint32_pair_float32_float32,
    (types['uint32'], types['pair_float64_float64']) : _gp.Dict_uint32_pair_float64_float64,
    (types['uint32'], types['bytearray2']) : _gp.Dict_uint32_bytearray2,
    (types['uint32'], types['bytearray4']) : _gp.Dict_uint32_bytearray4,
    (types['uint32'], types['bytearray8']) : _gp.Dict_uint32_bytearray8,
    (types['uint32'], types['bytearray10']) : _gp.Dict_uint32_bytearray10,
    (types['uint32'], types['bytearray16']) : _gp.Dict_uint32_bytearray16,
    (types['uint32'], types['bytearray20']) : _gp.Dict_uint32_bytearray20,
    (types['uint32'], types['bytearray30']) : _gp.Dict_uint32_bytearray30,
    (types['uint32'], types['bytearray32']) : _gp.Dict_uint32_bytearray32,
    (types['uint32'], types['bytearray40']) : _gp.Dict_uint32_bytearray40,
    (types['uint32'], types['bytearray50']) : _gp.Dict_uint32_bytearray50,
    (types['uint64'], types['str4']) : _gp.Dict_uint64_str4,
    (types['uint64'], types['str8']) : _gp.Dict_uint64_str8,
    (types['uint64'], types['str16']) : _gp.Dict_uint64_str16,
    (types['uint64'], types['str32']) : _gp.Dict_uint64_str32,
    (types['uint64'], types['uint8']) : _gp.Dict_uint64_uint8,
    (types['uint64'], types['uint16']) : _gp.Dict_uint64_uint16,
    (types['uint64'], types['uint32']) : _gp.Dict_uint64_uint32,
    (types['uint64'], types['uint64']) : _gp.Dict_uint64_uint64,
    (types['uint64'], types['int8']) : _gp.Dict_uint64_int8,
    (types['uint64'], types['int16']) : _gp.Dict_uint64_int16,
    (types['uint64'], types['int32']) : _gp.Dict_uint64_int32,
    (types['uint64'], types['int64']) : _gp.Dict_uint64_int64,
    (types['uint64'], types['float32']) : _gp.Dict_uint64_float32,
    (types['uint64'], types['float64']) : _gp.Dict_uint64_float64,
    (types['uint64'], types['pair_str4_str4']) : _gp.Dict_uint64_pair_str4_str4,
    (types['uint64'], types['pair_str8_str8']) : _gp.Dict_uint64_pair_str8_str8,
    (types['uint64'], types['pair_str16_str16']) : _gp.Dict_uint64_pair_str16_str16,
    (types['uint64'], types['pair_str32_str32']) : _gp.Dict_uint64_pair_str32_str32,
    (types['uint64'], types['pair_uint8_uint8']) : _gp.Dict_uint64_pair_uint8_uint8,
    (types['uint64'], types['pair_uint16_uint16']) : _gp.Dict_uint64_pair_uint16_uint16,
    (types['uint64'], types['pair_uint32_uint32']) : _gp.Dict_uint64_pair_uint32_uint32,
    (types['uint64'], types['pair_uint64_uint64']) : _gp.Dict_uint64_pair_uint64_uint64,
    (types['uint64'], types['pair_int8_int8']) : _gp.Dict_uint64_pair_int8_int8,
    (types['uint64'], types['pair_int16_int16']) : _gp.Dict_uint64_pair_int16_int16,
    (types['uint64'], types['pair_int32_int32']) : _gp.Dict_uint64_pair_int32_int32,
    (types['uint64'], types['pair_int64_int64']) : _gp.Dict_uint64_pair_int64_int64,
    (types['uint64'], types['pair_float32_float32']) : _gp.Dict_uint64_pair_float32_float32,
    (types['uint64'], types['pair_float64_float64']) : _gp.Dict_uint64_pair_float64_float64,
    (types['uint64'], types['bytearray2']) : _gp.Dict_uint64_bytearray2,
    (types['uint64'], types['bytearray4']) : _gp.Dict_uint64_bytearray4,
    (types['uint64'], types['bytearray8']) : _gp.Dict_uint64_bytearray8,
    (types['uint64'], types['bytearray10']) : _gp.Dict_uint64_bytearray10,
    (types['uint64'], types['bytearray16']) : _gp.Dict_uint64_bytearray16,
    (types['uint64'], types['bytearray20']) : _gp.Dict_uint64_bytearray20,
    (types['uint64'], types['bytearray30']) : _gp.Dict_uint64_bytearray30,
    (types['uint64'], types['bytearray32']) : _gp.Dict_uint64_bytearray32,
    (types['uint64'], types['bytearray40']) : _gp.Dict_uint64_bytearray40,
    (types['uint64'], types['bytearray50']) : _gp.Dict_uint64_bytearray50,
    (types['int32'], types['str4']) : _gp.Dict_int32_str4,
    (types['int32'], types['str8']) : _gp.Dict_int32_str8,
    (types['int32'], types['str16']) : _gp.Dict_int32_str16,
    (types['int32'], types['str32']) : _gp.Dict_int32_str32,
    (types['int32'], types['uint8']) : _gp.Dict_int32_uint8,
    (types['int32'], types['uint16']) : _gp.Dict_int32_uint16,
    (types['int32'], types['uint32']) : _gp.Dict_int32_uint32,
    (types['int32'], types['uint64']) : _gp.Dict_int32_uint64,
    (types['int32'], types['int8']) : _gp.Dict_int32_int8,
    (types['int32'], types['int16']) : _gp.Dict_int32_int16,
    (types['int32'], types['int32']) : _gp.Dict_int32_int32,
    (types['int32'], types['int64']) : _gp.Dict_int32_int64,
    (types['int32'], types['float32']) : _gp.Dict_int32_float32,
    (types['int32'], types['float64']) : _gp.Dict_int32_float64,
    (types['int32'], types['pair_str4_str4']) : _gp.Dict_int32_pair_str4_str4,
    (types['int32'], types['pair_str8_str8']) : _gp.Dict_int32_pair_str8_str8,
    (types['int32'], types['pair_str16_str16']) : _gp.Dict_int32_pair_str16_str16,
    (types['int32'], types['pair_str32_str32']) : _gp.Dict_int32_pair_str32_str32,
    (types['int32'], types['pair_uint8_uint8']) : _gp.Dict_int32_pair_uint8_uint8,
    (types['int32'], types['pair_uint16_uint16']) : _gp.Dict_int32_pair_uint16_uint16,
    (types['int32'], types['pair_uint32_uint32']) : _gp.Dict_int32_pair_uint32_uint32,
    (types['int32'], types['pair_uint64_uint64']) : _gp.Dict_int32_pair_uint64_uint64,
    (types['int32'], types['pair_int8_int8']) : _gp.Dict_int32_pair_int8_int8,
    (types['int32'], types['pair_int16_int16']) : _gp.Dict_int32_pair_int16_int16,
    (types['int32'], types['pair_int32_int32']) : _gp.Dict_int32_pair_int32_int32,
    (types['int32'], types['pair_int64_int64']) : _gp.Dict_int32_pair_int64_int64,
    (types['int32'], types['pair_float32_float32']) : _gp.Dict_int32_pair_float32_float32,
    (types['int32'], types['pair_float64_float64']) : _gp.Dict_int32_pair_float64_float64,
    (types['int32'], types['bytearray2']) : _gp.Dict_int32_bytearray2,
    (types['int32'], types['bytearray4']) : _gp.Dict_int32_bytearray4,
    (types['int32'], types['bytearray8']) : _gp.Dict_int32_bytearray8,
    (types['int32'], types['bytearray10']) : _gp.Dict_int32_bytearray10,
    (types['int32'], types['bytearray16']) : _gp.Dict_int32_bytearray16,
    (types['int32'], types['bytearray20']) : _gp.Dict_int32_bytearray20,
    (types['int32'], types['bytearray30']) : _gp.Dict_int32_bytearray30,
    (types['int32'], types['bytearray32']) : _gp.Dict_int32_bytearray32,
    (types['int32'], types['bytearray40']) : _gp.Dict_int32_bytearray40,
    (types['int32'], types['bytearray50']) : _gp.Dict_int32_bytearray50,
    (types['int64'], types['str4']) : _gp.Dict_int64_str4,
    (types['int64'], types['str8']) : _gp.Dict_int64_str8,
    (types['int64'], types['str16']) : _gp.Dict_int64_str16,
    (types['int64'], types['str32']) : _gp.Dict_int64_str32,
    (types['int64'], types['uint8']) : _gp.Dict_int64_uint8,
    (types['int64'], types['uint16']) : _gp.Dict_int64_uint16,
    (types['int64'], types['uint32']) : _gp.Dict_int64_uint32,
    (types['int64'], types['uint64']) : _gp.Dict_int64_uint64,
    (types['int64'], types['int8']) : _gp.Dict_int64_int8,
    (types['int64'], types['int16']) : _gp.Dict_int64_int16,
    (types['int64'], types['int32']) : _gp.Dict_int64_int32,
    (types['int64'], types['int64']) : _gp.Dict_int64_int64,
    (types['int64'], types['float32']) : _gp.Dict_int64_float32,
    (types['int64'], types['float64']) : _gp.Dict_int64_float64,
    (types['int64'], types['pair_str4_str4']) : _gp.Dict_int64_pair_str4_str4,
    (types['int64'], types['pair_str8_str8']) : _gp.Dict_int64_pair_str8_str8,
    (types['int64'], types['pair_str16_str16']) : _gp.Dict_int64_pair_str16_str16,
    (types['int64'], types['pair_str32_str32']) : _gp.Dict_int64_pair_str32_str32,
    (types['int64'], types['pair_uint8_uint8']) : _gp.Dict_int64_pair_uint8_uint8,
    (types['int64'], types['pair_uint16_uint16']) : _gp.Dict_int64_pair_uint16_uint16,
    (types['int64'], types['pair_uint32_uint32']) : _gp.Dict_int64_pair_uint32_uint32,
    (types['int64'], types['pair_uint64_uint64']) : _gp.Dict_int64_pair_uint64_uint64,
    (types['int64'], types['pair_int8_int8']) : _gp.Dict_int64_pair_int8_int8,
    (types['int64'], types['pair_int16_int16']) : _gp.Dict_int64_pair_int16_int16,
    (types['int64'], types['pair_int32_int32']) : _gp.Dict_int64_pair_int32_int32,
    (types['int64'], types['pair_int64_int64']) : _gp.Dict_int64_pair_int64_int64,
    (types['int64'], types['pair_float32_float32']) : _gp.Dict_int64_pair_float32_float32,
    (types['int64'], types['pair_float64_float64']) : _gp.Dict_int64_pair_float64_float64,
    (types['int64'], types['bytearray2']) : _gp.Dict_int64_bytearray2,
    (types['int64'], types['bytearray4']) : _gp.Dict_int64_bytearray4,
    (types['int64'], types['bytearray8']) : _gp.Dict_int64_bytearray8,
    (types['int64'], types['bytearray10']) : _gp.Dict_int64_bytearray10,
    (types['int64'], types['bytearray16']) : _gp.Dict_int64_bytearray16,
    (types['int64'], types['bytearray20']) : _gp.Dict_int64_bytearray20,
    (types['int64'], types['bytearray30']) : _gp.Dict_int64_bytearray30,
    (types['int64'], types['bytearray32']) : _gp.Dict_int64_bytearray32,
    (types['int64'], types['bytearray40']) : _gp.Dict_int64_bytearray40,
    (types['int64'], types['bytearray50']) : _gp.Dict_int64_bytearray50,
}
