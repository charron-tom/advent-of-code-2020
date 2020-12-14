import copy
from utils import MASK_BITS, dec2bin, bin2dec


class Mask(list):
    """
    A bitmask is represented as a list of tuples
    (index, bit) corresponding to what bit to write at
    what index.
    """

    def mask_addr(self, addr):
        """
        Return a binary address with the bitmask applied.
        """
        return dec2bin(addr, bits=len(self))

    def mask_value(self, value):
        """
        Return a decimal with the bitmask applied.
        """
        return value

    def _mask(self, b, bits):
        """
        Replace `bits` in a binary string `b`.
        """
        l = list(dec2bin(b, bits=len(self)))
        for i, bit in self:
            if bit in bits:
                l[i] = bit
        return "".join(l)

    @classmethod
    def create(cls, s):
        mask = cls()
        for i, bit in enumerate(s):
            mask.append((i, bit))
        return mask


class ValueMask(Mask):
    """
    Subclass of `Mask` that bitmasks the values being
    written into memory.
    """

    def mask_value(self, value):
        return bin2dec(self._mask(value, ['0', '1']), bits=len(self))


class AddressMask(Mask):
    """
    Subclass of `Mask` that bitmasks the memory addresses.
    """

    def mask_addr(self, addr):
        return self._mask(addr, ['1', 'X'])
