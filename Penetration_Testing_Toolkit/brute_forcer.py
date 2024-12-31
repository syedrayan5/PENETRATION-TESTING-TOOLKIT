import itertools

def brute_forcer(charset, max_length):
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            yield ''.join(guess)

# Usage
charset = 'abcdefghijklmnopqrstuvwxyz'
max_length = 4
for guess in brute_forcer(charset, max_length):
    print(guess)
