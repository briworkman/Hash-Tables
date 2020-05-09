def no_dups(s):
    # Implement me.
    split_string = s.split()
    cache = {}
    words = []

    for i in split_string:
        if i not in cache:
            cache[i] = 1
            words.append(i)
    return ' '.join(words)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
