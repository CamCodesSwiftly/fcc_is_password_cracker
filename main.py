# This entrypoint file to be used in development. Start by reading README.md
import password_cracker
from unittest import main

# cracked_password1 = password_cracker.crack_sha1_hash(
#     "b305921a3723cd5d70a375cd21a61e60aabb84ec")
# print(cracked_password1)

cracked_password2 = password_cracker.crack_sha1_hash(
    "53d8b3dc9d39f0184144674e310185e41a87ffd5", True)
print(cracked_password2)

# Run unit tests automatically
# main(module = "test_module", exit = False)
