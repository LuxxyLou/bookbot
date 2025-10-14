def get_num_words(text):
    words = text.split()
    return len(words)

def num_unique_chars(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return (chars)
