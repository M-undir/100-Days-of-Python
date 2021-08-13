# def fun():
#     return 3*2
#
# multiple = fun()
# print(multiple)

def initialized_name(f_name, l_name):
    # formatted_name = f"{f_name[0]}.{l_name[0]}"
    # return formatted_name
    if f_name == "" or l_name == "":
        return "Please enter your name CORRECTLY. "
    return f"{f_name.title()[0]}.{l_name.title()[0]}."


formatted_name = initialized_name(input("What is your first name? "), input("What is your last name? "))
print(formatted_name)
