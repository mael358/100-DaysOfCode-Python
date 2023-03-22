# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend"

PLACEHOLDER = "[name]"
starting_letter = ""
invited_names = []
END_OF_LINE = "\n"


# Get the invited names
with open("./Names/invited_names.txt") as file:
    invited_names = file.readlines()

# Read the starting letter
with open("./Letters/starting_letter.txt") as file:
    starting_letter = file.read()

# Create new letter for each invited
for name in invited_names:
    name = name.replace(END_OF_LINE, "")
    new_letter = starting_letter.replace(PLACEHOLDER, name)
    with open(f"./Output/ReadyToSend/{name}_invite.txt", "w") as file:
        file.write(new_letter)
