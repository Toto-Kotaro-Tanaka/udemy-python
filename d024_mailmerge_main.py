PLACEHOLDER = "[name]"

with open("./d024_Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)
    
with open("./d024_Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, strip_name)
        print(new_letter)
        with open(f"./d024_Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)