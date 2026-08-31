def shift_words(text, price):
    new_text = ""
    letters = 0

    for letter in text:
        if letter == " ":
            new_text = new_text + " "
        else:
            new_text = new_text + chr(ord(letter) + 1)
            letters = letters + 1

    words = len(text.split())
    total_price = letters * price

    result = {
        "shifted_string": new_text,
        "word_count": words,
        "price": total_price
    }

    return result


print(shift_words("hello world", 2))