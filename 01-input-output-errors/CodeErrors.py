# # print("Hello World)  -> jutumärgid lõpetamata
#
# # Taande viga (Unexpected indent)
# #    print("Hello")
#
# # print(undeclared) -> Name error (defineerimata muutuja kutsumine)
#
# # variable = "viis"
# # print(variable + 10)  -> will trow TypeError: incompatible types
#
#
#
# def third(a):
#     print(int(a))  # Attempt to convert string <The output is called 'Stack Trace'> to int and print it out
#
#
# def second(a, b):
#     c = a + b
#     print(c)  # --> The output is called 'Stack Trace'
#
#     # Calling the third function
#     third(c)
#
#
# def first():
#     # Calling the second function
#     second("The output is called ", "'Stack Trace'")
#
# first()