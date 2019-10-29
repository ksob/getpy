import numpy as np

import _getpy as _gp

types = {
    'uint8' : np.dtype('u1'),
    'uint64' : np.dtype('u8'),
}

dict_types = {
    (types['uint64'], types['uint8']) : _gp.Dict_uint64_uint8,
}

set_types = {
}
