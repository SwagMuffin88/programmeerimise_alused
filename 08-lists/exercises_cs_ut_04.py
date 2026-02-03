"""https://courses.cs.ut.ee/t/pythonkoolis/Main/JarjendYl"""
from random import randint


# Ex. 3
def translate_numbers():
    numbers = [1, 2, 3, 4]
    estonian = ["üks", "kaks", "kolm", "neli"]
    english = ["one", "two", "three", "four"]
    italian = ["uno", "due", "tre", "quattro"]


    print(f"Num|  EST  |  ENG  | IT")
    for i in range(len(numbers)):
        print(f" {numbers[i]} |  {estonian[i]:^4} | {english[i]:^5} | {italian[i]:^7}")


# Ex. 4
def generate_magic_ball_answer():
    print("Küsi mult ükskõik, millist jah/ei küsimust ja ma tean vastust!")
    question = input("Please enter your question: ")

    while question != "":
        answer_options = ["Jah, kindlasti!", "Jah!", "Võib-olla!", "Ei!"]
        answer_index = randint(0, len(answer_options) - 1)
        print(answer_options[answer_index])
        question = input("Ask another question or press enter to quit: ")
        if question == "":
            print("Loodan, et sul oli tore! Nägemist!")
            break




if __name__ == '__main__':
    #translate_numbers()
    generate_magic_ball_answer()