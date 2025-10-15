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

def sort_chars(text):    
    sorted_chars = sorted(text.items(), key=lambda item: item[1], reverse=True)
    result = ""
    for char, count in sorted_chars:
        if char == "\n":
            display_char = "\\n"
        elif char == " ":
            display_char = "' '"
        else:
            display_char = char
        result += f"'{display_char}': {count}\n"
    return result

def get_report(text):
    num_words = get_num_words(text)
    num_chars = num_unique_chars(text)
    sorted_chars = sort_chars(text)
    return f"Word Count: {num_words}\nUnique Characters: {num_chars}\nCharacter Frequency:\n{sorted_chars}"