from dictionaries import morse_code_dict

persian_numbers = {'۰': '– – – – –',
                   '۱': '• – – – –',
                   '۲': '• • – – –',
                   '۳': '• • • – –',
                   '۴': '• • • • –',
                   '۵': '• • • • •',
                   '۶': '– • • • •',
                   '۷': '– – • • •',
                   '۸': '– – – • •',
                   '۹': '– – – – •',
                   }


def input_ask():
    conversion_type = input(
        "input ('d' to decode a morse code.) & \n ('e' to encode English to morse) \n Type Here: ").lower()
    if conversion_type == 'd':
        input_text = input("Write in Morse: \n (Use '/' instead of spaces between words) \n Type Here:  ")
        decode(input_text)
    elif conversion_type == 'e':
        input_text = input("Write in English: ")
        encode(input_text)
    else:
        print("It was not in the instruction \n initialize again.")


def encode(input_text):
    try:
        morse = [morse_code_dict[alp] for alp in list(input_text.upper())]
        enc = ' '.join(sign for sign in morse)
    except KeyError as e:
        print(f"The character {e.args[0]} is not defined by morse code, remove it and try again!")
    finally:
        print(enc)


def decode(input_text):
    dec = ''
    for sign in input_text.split(' '):
        if sign == '/':
            sign = ' / '
        for key, value in morse_code_dict.items():
            if value == sign:
                dec += key
                break
            else:
                continue
    print(dec.capitalize())


if __name__ == "__main__":
    input_ask()
