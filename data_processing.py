import numpy as np

def int_from_bytes(byte_s):
    return int.from_bytes(byte_s, "big")

def bin_array_to_float32(bin_array):
    return np.array(bin_array).astype(np.float32)

def float_array_to_hex(array, fill):
    binary_string = ''.join(['1' if bit > 0.5 else '0' for bit in array])
    hex_value = hex(int(binary_string, 2))[2:].zfill(fill)
    return hex_value

def convert_to_binary(element, bits):
    binary = bin(element)[2:].zfill(bits)
    return [int(bit) for bit in binary]

def convert_to_binary_arrays(given_array, bits):
    return [convert_to_binary(element, bits) for element in given_array]
