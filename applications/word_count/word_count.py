def word_count(s):
    # Implement me.
    lower_string = s.lower()
    split_string = [''.join([c for c in w if c.isalpha() or c == "'"])
                    for w in lower_string.split()]
    cache = {}
    for i in split_string:
        if i not in cache:
            cache[i] = 1
        elif i in cache:
            cache[i] += 1
        else:
            return None
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
