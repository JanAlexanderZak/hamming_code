import numpy as np
from functools import reduce
np.random.seed(7)


class SimulateHammingCode:

    def __init__(self, _bits):
        self.bits: np.ndarray = _bits

    def send_bits(self) -> np.ndarray:
        """ Alters a bit at a random position
        :param _bits: _bits where one bit is to be altered
        :return: altered list of bits
        """
        random_index: int = np.random.randint(0, self.bits.shape[0])  # 15
        if self.bits[random_index] == 1:
            self.bits[random_index] = 0
        else:
            self.bits[random_index] = 1
        return self.bits

    def prepare_bits(self) -> None:
        """ Alters list of bits that the parity check is 0
        :param _bits:
        :return:
        """
        error_bit = self.parity_check(self.bits)
        print("Parity check before preperation: ", error_bit)
        error_bit = bin(error_bit)[2:].rjust(4, '0')

        # Get integer index
        row = int(f'{error_bit[0:2]}00', 2)
        column = int(f'00{error_bit[2:4]}', )

        # Replace bits
        self.bits[row] = not self.bits[row]
        self.bits[column] = not self.bits[column]

        print("Parity check after preperation: ", self.parity_check(self.bits))
        return None

    def parity_check(self, _bits) -> int:
        return reduce(lambda x, y: x ^ y, [i for i, bit in enumerate(_bits) if bit])


if __name__ == '__main__':
    bits = np.array([0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1])

    simualtion = SimulateHammingCode(bits)
    error_location = simualtion.parity_check(bits)
    print("Error location of unprepared bits: ", error_location)
    simualtion.prepare_bits()
    send_bits = simualtion.send_bits()
    error_location = simualtion.parity_check(send_bits)
    print("Error location of send bits", error_location)
