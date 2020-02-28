""" User Interface (UI) module """
from os import system, name

def clear():
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')

def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
clear()
lenght_of_element = title_list[0]
lenght_of_elements_title_list = []
for i in range(len(title_list)): 
    lenght_of_elements_title_list.append(len(title_list[i]))

lenght_of_elements_table = []

for i in range(len(table[0])):
    longest = 0
    for j in range(len(table)):
        if longest < len(table[j][i]):
            longest = len(table[j][i])
    lenght_of_elements_table.append(longest)
number_of_element_in_table = len(table)

last_result = []
for i in range(len(lenght_of_elements_title_list)):
    if lenght_of_elements_title_list[i] <= lenght_of_elements_table[i]:
        temp = lenght_of_elements_table[i]
    else:
        temp = lenght_of_elements_title_list[i]
    last_result.append(temp)

separator = ' | '
lenght_of_separator = len(separator)

summa = 0
for i in last_result:
    summa += i


number_of_separator = len(last_result) - 1

line = (summa + (number_of_separator * lenght_of_separator) + 2) * '-'


print(f' /{line}\\ ')

print(separator, end='')
for j in range(len(title_list)):
    print(f'{title_list[j]:^{last_result[j]}}', end='')
    if j != (len(title_list) - 1):
        print (separator, end='')
print(separator)

for i in range(len(table)):
    print(f' |{line}|')
    print(separator, end='')
    for j in range(len(last_result)):
        print(f'{table[i][j]:^{last_result[j]}}', end='')
        if j != (len(last_result)-1):
            print (separator, end='')
    print(separator)
print(f' \{line}/')
    


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    pass

def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(f'{title}:')
    for i in range (len(list_options)):
        print(f'    ({i+1}) {list_options[i]}')
    print(f'    (0) {exit_message}')


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    for i in list_labels:
        clear()
        print(title)
        user_answer = input(f'{i}:')
        inputs.append(user_answer)

    return inputs

    


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f'Error: {message}')