# https://courses.cs.ut.ee/t/pythonkoolis/Main/SonastikYl


# Ex. 1
est_it = {"auto": "auto", "koer": "cane", "kass": "gatto", "tere": "ciao"}
est_eng = {"auto": "car", "koer": "dog", "kass": "cat", "tere": "hello"}

est_it["üks"] = "uno"
est_eng["kolm"] = "three"


#Ex. 3
def convert_dict_reverse(dict_a: dict) -> dict:
    # return {value: key for key, value in dict_a.items()} -> lühem varjant
    new_dict = {}
    for key, value in dict_a.items():
        new_dict[value] = key

    return new_dict


# Ex. 4
def add_new_word_to_dict(dict_a: dict, key_word:str, value_word:str) -> None:
    dict_a[key_word] = value_word


def add_multiple_new_words_to_dict(dict_a: dict, key_list: list, value_list: list) -> None:
    for i in range(len(key_list)):
        add_new_word_to_dict(dict_a, key_list[i], value_list[i])


#Ex. 5
def translate_into_morse(_input: str) -> str:
    alphabet = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                "y": "-.--", "z": "--.."}

    special_chars = {"ž": "z", "š": "s", "õ": "o", "ä": "a", "ö": "o", "ü": "u"}

    output: str = ""
    _input = _input.lower()

    for character in _input:
        if character in special_chars.keys():
            output = output + alphabet.get(
                special_chars.get(character)
                    ) + " "
        else:
            output = output + alphabet.get(character) + " "

    return output


def create_morse_from_input(text: str) -> str:
    return translate_into_morse(text)


def greet_in_morse(name:str) -> str:
    morse_greeting = translate_into_morse("Tere") + translate_into_morse(name)
    return f"Tere, {name}! \n {morse_greeting}"


def greet_user_and_translate_user_input_to_morse() -> str:
    name = input("Please enter your name: ")
    print(greet_in_morse(name))
    text = input("Try translating some words into morse: ")
    output = ""

    while text != "":
        output = translate_into_morse(text)
        print(output)
        text = input("Try another one: ")

    print("This morse code program has ended.")


if __name__ == '__main__':
    # Ex. 2:
    print(f"tere -> inglise keeles {est_eng.get("tere")}, itaalia keeles {est_it.get("tere")}")
    print(f"auto -> itaalia keeles {est_it.get("auto")}")
    print(f"kass -> inglise keeles {est_eng.get("kass")}")
    print(f"üks -> itaalia keeles {est_it.get("üks")}")
    print(f"kolm -> inglise keeles {est_eng.get("kolm")}")

    # add_new_word_to_dict(est_eng, "head aega", "goodbye")
    # add_new_word_to_dict(est_it, "head aega", "arrivederci")

    new_est_words = ["head aega", "pott", "sõnastik"]
    add_multiple_new_words_to_dict(
        est_eng,
        new_est_words,
        ["good bye", "pot", "dictionary"]
    )

    add_multiple_new_words_to_dict(
        est_it,
        new_est_words,
        ["arrivederci", "pentola", "dizionario"]
    )

    it_est = convert_dict_reverse(est_it)
    eng_est = convert_dict_reverse(est_eng)
    print(est_eng)
    print(est_it)
    print(it_est)
    print(eng_est)

    """
    üks -> itaalia
    ciao - > eesti
    dog -> itaalia
    pentola - inglise
    """
    print(f"üks -> itaalia keeles {est_it.get("üks")}")
    print(f"ciao -> eesti keeles {it_est.get("ciao")}")
    print(f"dog -> itaalia keeles "
          f"{est_it.get(
              eng_est.get("dog"))
          }")
    print(f"pentola -> inglise keeles "
          f"{est_eng.get(
              it_est.get("pentola"))
          }")

    greet_user_and_translate_user_input_to_morse()