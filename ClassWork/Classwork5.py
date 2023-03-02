g = 5
a = "helloworld"
p = 23
a_len = 0

for character in a:
    a_len += ord(character)


alice = (g ** a_len) % p
print("Shared Key for Alice is " + str(alice))


shared_key = int(input("Enter Bob Key:- "))
alice_key = (shared_key ** a_len) % p

print(alice_key)



