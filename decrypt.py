from Crypto.Util.number import long_to_bytes

def rsa_decrypt(ciphertext_hex, n_hex, d_hex):
    try:
        n = int(n_hex, 16)
        d = int(d_hex, 16)
        ciphertext = int(ciphertext_hex, 16)

        plaintext = pow(ciphertext, d, n)

        return long_to_bytes(plaintext).decode('utf-8')
    except ValueError as ve:
        return f"Error during decryption: {ve}"
    except Exception as e:
        return f"Unexpected error: {e}"

def main():
    # RSA private key components (modulus n and private exponent d) in hexadecimal format
    n_hex = "0xaf019690974da7fcf99202ce4202843fd446bf67b470812518133904595d15cfed6d7f38064da9e881fefff88e1193a142cfa78ddc0a991aabef8818d7e88248cc3a573e4830f7e55fb047549609caf5f3e3e3a7da5f4dc51ce1122fd921dd9906e649b1a7cd8e8623116bc52ad5262bc4cffd7a1e1f824bcbcaa0003e9c1573"
    d_hex = "0x7b77f65f0ab05a0d8b922cf291f5ae924dd4a023ad551678323515abf0d4509842dd56bd130d660b48f3bc6a02e979ab733487f4f8c26d6438dba4bc4a4f9ae2509ecdcc673e3cb66866f8f6e79c66a7b81222ad5b31ee9dd885320868ed0992dc1b667cdc69e9a720bb7a4d131498d911e1f9805ce26fa6c79f0bea281e4911"
    
    # Ciphertext to decrypt in hex
    ciphertext_hex = "0x960fc174f3cdf0e7d9d4e7b6d08193aafe472e8481cdd4aa5ee7f60aa13f443b58d173842e479fb6ec39bf0fbf3490100a530202ed4b03a4e25a6f8fa57c97659a5e75ddab27306b7577157a0eaf26c695364d56abee2196933eb1b31089b2fc59bc538906eb03bb9c96617fa114330bc9e6312d7339105d581e8e9f567714cc"

    # Decrypt the ciphertext
    decrypted_message = rsa_decrypt(ciphertext_hex, n_hex, d_hex)

    # Print the decrypted message or an error if it occurred
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
