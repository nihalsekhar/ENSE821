import random


def get_message(message, seed):
    i = 1
    rand_num = []
    len_message = len(message)
    random.seed(seed)
    while len_message > 1:
        len_message = len_message - 1
        j = random.randrange(len_message)
        rand_num.append(j)
    while i < len(message):
        j = rand_num.pop()
        message[j], message[i] = message[j], message[i]
        i += 1
    return message

message = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
seed = 12345

print(get_message(message, seed))
