from cryptography.fernet import Fernet


def decrypting():
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    store = Fernet(key)

    with open("encrypted_keylog.txt", "rb") as read_encrypt:
        encrypted = read_encrypt.read()

    decrypted = store.decrypt(encrypted)

    with open("decrypted_keylog.txt", "wb") as write_decrypt:
        decrypted = write_decrypt.write(decrypted)
