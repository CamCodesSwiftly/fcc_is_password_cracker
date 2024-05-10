import hashlib

def read_passwords():
    with open("top-10000-passwords.txt", "r") as file:
        passwords = [line.strip() for line in file.readlines()]
    return passwords

def read_salts():
    with open("known-salts.txt", "r") as file:
        salts = [line.strip() for line in file.readlines()]
    return salts

def hash_passwords(passwords):
    hashed_passwords = []
    for password in passwords:
        password_bytes = password.encode("utf-8")
        sha1_hash = hashlib.sha1()
        sha1_hash.update(password_bytes)
        hashed_password = sha1_hash.hexdigest()
        hashed_passwords.append(hashed_password)
    return hashed_passwords

def crack_sha1_hash(hash, use_salts = False):
    # read 10k passwords
    passwords = read_passwords()

    # hash 10k passwords
    hashed_passwords = hash_passwords(passwords)

    # check if the password is in the list
    if use_salts:
        salts = read_salts()
        salted_passwords = hash_passwords_with_salts(passwords, salts)

        #TODO: did the appending/prepending go wrong?
        print(hash)
        print(passwords[salted_passwords.index(hash)])
        if hash in salted_passwords:
            return passwords[salted_passwords.index(hash)]
        #TODO: did the appending/prepending go wrong?

    else:
        if hash in hashed_passwords:
            return passwords[hashed_passwords.index(hash)]
        else:
            return "PASSWORD NOT IN DATABASE"


def hash_password_with_salt(password, salt):
    combined = salt + password + salt
    hashed = hashlib.sha1(combined.encode()).hexdigest()
    return hashed

def hash_passwords_with_salts(passwords, salts):
    hashed_passwords = []
    for password in passwords:
        for salt in salts:
            hashed = hash_password_with_salt(password, salt)
            hashed_passwords.append(hashed)
    return hashed_passwords