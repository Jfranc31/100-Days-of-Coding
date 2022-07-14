with open("Input/Names/invited_names.txt") as names:
    with open("Input/Letters/starting_letter.txt") as letter:
        letter_txt = letter.read()
        name = names.readlines()
        final_names = []
        for _ in name:
            final_names.append(_.strip())

        for name in final_names:
            file = open(f"Output/ReadyToSend/letter_to_{name}.txt", mode="w")
            new_letter = letter_txt.replace("[name]", name)
            file.write(new_letter)
            file.close()

