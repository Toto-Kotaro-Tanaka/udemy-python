# file = open("d24_text.txt")
# contents = file.read()
# print(contents)
# file.close()


# Opening file with "with" key word

# with open("d24_text.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing text in file

with open("d24_text.txt", mode="a") as file:
    file.write("\nNew New text")