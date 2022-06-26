# Read the invited_names.text file.
with open("E:/Python/Python/Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as file:
    contents = (file.readlines())

list_of_names = []

for names in range(len(contents)):
    # Checking for the new line in the list element.
    if "\n" in contents[names]:
        # If a new line character is found, then it is going to be replaced with "".
        list_of_names.append(contents[names].replace("\n", ""))
    else:
        list_of_names.append(contents[names])


# Read the starting_letter.txt file and make a list.
with open("E:/Python/Python/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as file:
    contents = file.readlines()


for text in range(len(list_of_names)):
    for letter in range(len(contents)):
        # Writing the files in this directory.
        with open(f"E:/Python/Python/Mail Merge Project Start/Output/ReadyToSend/{list_of_names[text]}.txt", mode="a") as file:
            if "[name]" in contents[letter]:
                # Replacing the "[name]" with the list names.
                file.write(contents[letter].replace("[name]", list_of_names[text]))
            else:
                file.write(contents[letter])

