from dict_resource import MORSE_CODE_DICT


def convert_text(input_list):
    output_list = []
    for letter in input_list:
        upper = letter.upper()
        output_list.append(MORSE_CODE_DICT[upper])
    # join the list with space to form the morse code
    output = ' '.join(output_list)
    return print(output)


while True:
    # take the user input
    input_text = input('Input Text: ')

    # split string into list
    input_text_list = [*input_text]

    try:
        convert_text(input_text_list)
    except KeyError:
        print("Please input correctly.")
        