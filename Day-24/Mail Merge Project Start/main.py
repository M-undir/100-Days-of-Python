# TODO: Create a letter using starting_letter.txt
# for each  name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# main_path = /100-Days-Of-Python/Day-24/Mail Merge Project Start
# name_path = /Day-24/Mail Merge Project Start/Input/Names

# Put names in a list
# names = []
# with open('Input/Names/invited_names.txt') as invited_names:
#     # for _ in invited_names:
#     #     names.append(_.strip())
#     names = [name.strip() for name in invited_names]

# print(names)

# with open('Input/Letters/starting_letter.txt', mode='a') as starting_letter:
#   contents = starting_letter.read()
#   print(contents)
#   info = [f.strip() for f in starting_letter]
#   starting_letter.write()
#   print(info)

# with open('Input/Letters/starting_letter.txt', mode='r') as starting_letter:
#     list_of_lines = starting_letter.readlines()
#     for i in range(len(names) - 1):
#         name = names[i]
#         list_of_lines[0] = f"Dear {name},\n "
#         with open(f'Output/ReadyToSend/{name}', mode='w') as starting_l:
#             starting_l.writelines(list_of_lines)


with open('Input/Names/invited_names.txt') as invited_names:
    # for _ in invited_names:
    #     names.append(_.strip())
    names = [name.strip() for name in invited_names]
    # a condensed for loop

with open('Input/Letters/starting_letter.txt', mode='r') as starting_letter:
    content = starting_letter.read()
    # list_of_lines = starting_letter.readlines()
    for name in names:
        # list_of_lines[0] = f"Dear {name},\n "
        new_letter = content.replace('[name]', name)
        with open(f'Output/ReadyToSend/letter_for_{name}', mode='w') as finished_letter:
            # starting_l.writelines(list_of_lines)
            finished_letter.writelines(new_letter)

# Save three lines of code when using Angela's method.
# There is no right solution - aim for readability
