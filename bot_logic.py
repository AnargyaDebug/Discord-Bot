import random

def random_word(length):
    elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    generated = ""

    for _ in range(length):
        generated += random.choice(elements)

    return generated
