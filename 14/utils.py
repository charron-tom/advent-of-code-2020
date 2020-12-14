import copy


MASK_BITS = 36


def pad(s, bits=MASK_BITS):
    """
    Pad a string with the appropriate amount of bits.
    """
    n = bits - len(s)
    return ("0" * n) + s


def dec2bin(dec, bits=MASK_BITS):
    """
    Convert a decimal to a binary.
    """
    s = bin(int(dec)).replace("0b", "")
    return pad(s, bits=bits)


def bin2dec(b, bits=MASK_BITS):
    """
    Convert a binary to a decimal.
    """
    dec = 0
    for i, bit in enumerate(b):
        if bit == '1':
            dec += 2 ** (bits - i - 1)
    return dec


def bin2dec_floating(b, bits=MASK_BITS):
    """
    Convert a binary to a series of decimals,
    taking into account "floating" bits.
    """
    for i, bit in enumerate(list(b)):
        if bit == 'X':

            b0 = list(copy.copy(b))
            b0[i] = '0'

            b1 = list(copy.copy(b))
            b1[i] = '1'

            return bin2dec_floating("".join(b0), bits=bits) + bin2dec_floating("".join(b1), bits=bits)
    return [bin2dec(b, bits=bits)]
