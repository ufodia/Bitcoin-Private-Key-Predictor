import random
from bit.crypto import ECPrivateKey, ripemd160_sha256
from data_processing import int_from_bytes, convert_to_binary_arrays, bin_array_to_float32

def generate_training_data(length, seed, bits_secret=256, bits_p2pkh=160):
    secrets = []
    x_uncompressed = []
    x_compressed = []
    x_segwit = []

    random.seed(seed)
    
    for _ in range(length):
        secret_key = random.getrandbits(bits_secret)
        secrets.append(secret_key)
        
        private_key = ECPrivateKey.from_int(secret_key)
        pub_uncompressed = private_key.public_key.format(compressed=False)
        pub_compressed = private_key.public_key.format(compressed=True)

        hash_uncompressed = ripemd160_sha256(pub_uncompressed)
        hash_compressed = ripemd160_sha256(pub_compressed)
        hash_segwit = ripemd160_sha256(b'\x00\x14' + ripemd160_sha256(pub_compressed))

        x_uncompressed.append(int_from_bytes(hash_uncompressed))
        x_compressed.append(int_from_bytes(hash_compressed))
        x_segwit.append(int_from_bytes(hash_segwit))

    secrets_binary = convert_to_binary_arrays(secrets, bits_secret)
    x_uncompressed_binary = convert_to_binary_arrays(x_uncompressed, bits_p2pkh)
    x_compressed_binary = convert_to_binary_arrays(x_compressed, bits_p2pkh)
    x_segwit_binary = convert_to_binary_arrays(x_segwit, bits_p2pkh)

    return (
        bin_array_to_float32(secrets_binary),
        bin_array_to_float32(x_uncompressed_binary),
        bin_array_to_float32(x_compressed_binary),
        bin_array_to_float32(x_segwit_binary),
    )
