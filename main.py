with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("Input/Names/invited_names.txt", "r") as file:
    lines = file.readlines()
    names = []
    for line in lines:
        names.append(line.strip())

for name in names:
    with open(f"Output/ReadyToSend/invite_for_{name}", "w") as file:
        new_letter = letter.replace("[name],", name)
        file.write(new_letter)