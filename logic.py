import random
import time


def generate_sequence(level):
    sequence = [random.randint(1, 4) for _ in range(level)]
    return sequence


def display_sequence(sequence):
    print("\nMemorize the following sequence:")
    print(" ".join(str(x) for x in sequence))
    time.sleep(len(sequence) * 0.75)
    print("\033[H\033[J")  # Clear console


def get_user_input(level):
    print(f"Enter the sequence of length {level}:")
    user_input = list(map(int, input().split()))
    return user_input
