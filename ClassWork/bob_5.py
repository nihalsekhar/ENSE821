p = 23
b = "goodnight"
g = 5
b_len = 0

for character in b:
    b_len += ord(character)

bob = (g ** b_len) % p

print("Shared Key for Bob is :- " + str(bob))

shared_key = int(input("Alice's shared key :- "))
bob_key = (shared_key ** b_len) % p
print("KEY IS :- " + str(bob_key))
