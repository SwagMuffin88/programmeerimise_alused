"""String exercises."""

# 1.
first_name = "James"
last_name = "Bond"

# 2.
full_name = first_name + " " + last_name
self_description_sentence = f"My name is {last_name}, {first_name} {last_name}."

# 3.
cake = "vahukoormarjadtäidispõhi"
# print("vahukoor\nmarjad\ntäidis\npõhi")


# 4.
original_string = "Programming is fun!"
backwards = original_string[::-1]
every_other = original_string[::2]
first_word_reversed = original_string[10::-1]


if __name__ == '__main__':
    # name = "snow storm"
    # two = "two"
    #
    # my_list = ["Hello", "World", "Again"]
    # # sorted(my_list)
    # my_list.sort()
    # print("".join(my_list))

    print(every_other)
    print(backwards)
    print(first_word_reversed)
    print("vahukoor\nmarjad\ntäidis\npõhi")
