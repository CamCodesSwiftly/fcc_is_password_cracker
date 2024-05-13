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
        # salt the password list
        salts = read_salts()
        result = hash_passwords_with_salts(passwords, salts, hash)
        return result
    else:
        if hash in hashed_passwords:
            return passwords[hashed_passwords.index(hash)]
        else:
            return "PASSWORD NOT IN DATABASE"




def hash_passwords_with_salts(passwords, salts, hash):
    hashed_passwords = []
    for password in passwords:
        salted = password
        for salt in salts:
            left_salted = salt + salted
            right_salted = salted + salt
            hashed_left_salted = hashlib.sha1(left_salted.encode()).hexdigest()
            hashed_right_salted = hashlib.sha1(right_salted.encode()).hexdigest()
            if hashed_left_salted == hash or hashed_right_salted == hash:
                return password
    return False

#cabd3202661a89b6fb4daa806c942113e44db847