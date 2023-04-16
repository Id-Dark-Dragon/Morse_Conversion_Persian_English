from dictionaries import morse_code_persian_dict, morse_code_english_dict


def input_ask():
    input_lan_selection = input("input 'e' for english conversions \nبرای تبدیل فارسی حرف 'f' را وارد کنید \n : ").lower()
    while True:
        if input_lan_selection == "e":
            print("___________________________________")
            conversion_type = input(
                "input ('d' to decode a morse code.) & \n ('e' to encode English to morse) \n Type Here: ").lower()
            if conversion_type == 'd':
                input_text = input("Write in Morse: \n (Use '/' instead of spaces between words) \n Type Here:  ")
                decode(input_text, "e")
            elif conversion_type == 'e':
                input_text = input("Write in English: ")
                encode(input_text, "e")
            else:
                print("It was not in the instruction \n initialize again.")

        elif input_lan_selection == "f":
            print("___________________________________")
            conversion_type = input("برای تبدیل فارسی به مورس 'م' را وارد کنید \n برای تبدیل مورس به فارسی 'ف' را وارد کنید \n گزینه انتخابی: ").lower()
            if conversion_type == 'ف':
                input_text = input(" کد مورس را وارد کنید. مطمين شوید که بین کلمات یک جمله '/' وجود دارد. \n  در اینجا وارد کنید: ")
                decode(input_text, "f")
            elif conversion_type == 'م':
                input_text = input(" متن را وارد کنید: ")
                encode(input_text, "f")
            else:
                print("فرمان یافت نشد.")


def encode(input_text, language):
    enc = None
    if language == "e":
        try:
            morse = [morse_code_english_dict[alp] for alp in list(input_text.upper())]
            enc = ' '.join(sign for sign in morse)
        except KeyError as e:
            print(f"The character {e.args[0]} is not defined by morse code, remove it and try again!")
        finally:
            print(enc)

    elif language == "f":
        try:
            morse = [morse_code_persian_dict[alp] for alp in list(input_text)]
            enc = ' '.join(sign for sign in morse)
        except KeyError as e:
            print(f"The character {e.args[0]} is not defined by morse code, remove it and try again!")
        finally:
            print(enc)


def decode(input_text, language):
    dec = ''
    if language == "e":
        for sign in input_text.split(' '):
            if sign == '/':
                sign = ' / '
            for key, value in morse_code_english_dict.items():
                if value == sign:
                    dec += key
                    break
                else:
                    continue
        print(dec.capitalize())

    if language == "f":
        for sign in input_text.split(' '):
            if sign == '/':
                sign = ' / '
            for key, value in morse_code_persian_dict.items():
                if value == sign:
                    dec += key
                    break
                else:
                    continue
        print(dec)


if __name__ == "__main__":
    input_ask()
