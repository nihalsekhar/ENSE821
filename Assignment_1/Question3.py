import random
from random import randint


def shuffling_cipher(message, seed):
    random.seed(seed)
    msg_len = range(0, len(message))
    for i in msg_len:
        j = randint(msg_len[0], msg_len[-1])
        message[i], message[j] = message[j], message[i]
    return message


message = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
seed = 12345
print(shuffling_cipher(message, seed))
