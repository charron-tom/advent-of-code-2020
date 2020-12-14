from utils import bin2dec, bin2dec_floating


class Memory(dict):

    def __init__(self):
        self._mask = None

    @property
    def mask(self):
        return self._mask

    @mask.setter
    def mask(self, mask):
        self._mask = mask

    def sum(self):
        """
        Compute the sum of all the values in memory.
        """
        memory = 0
        for k in self:
            memory += self[k]
        return memory

    def __setitem__(self, key, value):
        """
        When writing data into memory, apply the appropriate
        bitmasking on the address and any values.
        """
        masked_addr = self.mask.mask_addr(key)
        for addr in bin2dec_floating(masked_addr):
            dict.__setitem__(self, addr, self.mask.mask_value(value))

