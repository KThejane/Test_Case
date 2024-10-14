from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key.key", "wb") as keyFile:
    keyFile.write(key)


fernet = Fernet(key)

with open("accesscode.csv", "rb") as tf:
    tf_bytes = tf.read()

tf_bytes_enc =  fernet.encrypt(tf_bytes)

with open("accesscode.csv", "wb") as tf:
    tf.write(tf_bytes_enc)