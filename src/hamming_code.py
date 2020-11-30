import numpy as np
from functools import reduce
np.random.seed(7)


def send_bits(_bits: np.array):
    """ Alters a bit at a random position
    :param _bits: _bits where one bit is to be altered
    :return: altered list of bits
    """
    random_index: int = np.random.randint(0, _bits.shape[0])  # 15
    if _bits[random_index] == 1:
        _bits[random_index] = 0
    else:
        _bits[random_index] = 1
    return _bits


def prepare_bits(_bits: np.array):
    """ Alters list of bits that the parity check is 0
    :param _bits:
    :return:
    """
    error_bit = parity_check(_bits)
    print("Parity check before preperation: ", error_bit)
    error_bit = bin(error_bit)[2:].rjust(4, '0')

    # Get integer index
    row = int(f'{error_bit[0:2]}00', 2)
    column = int(f'00{error_bit[2:4]}', )

    # Replace bits
    _bits[row] = not _bits[row]
    _bits[column] = not _bits[column]

    # Failcheck
    print("Parity check after preperation: ", parity_check(_bits))
    return _bits


def parity_check(_bits):
    return reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(_bits) if bit])


if __name__ == '__main__':
    bits = np.array([0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1])
    print(bits)

    prepared_bits = prepare_bits(bits)
    print("Matrix representation: \n", prepared_bits.reshape(4, 4))

    send_bits_ = send_bits(prepared_bits)  # alters at index=15, last element
    print(send_bits_)
    print("Matrix representation: \n", send_bits_.reshape(4, 4))
    x = parity_check(send_bits_)
    print(x)
