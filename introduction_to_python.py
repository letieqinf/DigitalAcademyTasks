def welcome_to_python(user_name: str, user_last_name: str) -> str:
    return 'Hello %s %s! You just delved into Python. Great start!' % (user_name, user_last_name)


def python_art(marker: str, thickness: int) -> None:
    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

        # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

        # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c +
               (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

    print(end='\n\n')


def title(string: str) -> str:
    return string.title()


def formatted_money(money_sum: float) -> str:
    return f'{money_sum:,.2f}'


def carpet_designer(width: int) -> None:
    length = 3 * width

    print(('_' * length).center(length))

    for pattern_counter in range(3, width, 2):
        print('|'.ljust(0) + ('/=' + '|=' * pattern_counter + '\\').center(length - 2) + '|'.rjust(0))

    print('|'.ljust(0) + 'WELCOME'.center(length - 2, '=') + '|'.rjust(0))

    for pattern_counter in range(width - 2, 2, -2):
        print('|'.ljust(0) + ('\\=' + '|=' * pattern_counter + '/').center(length - 2) + '|'.rjust(0))

    print(('\u203e' * length).center(length), end='\n\n')


def multiply_digits(number: int) -> int:
    if number == 0:
        return 0

    mult = 1
    for digit in list(map(int, str(number))):
        if digit != 0:
            mult *= digit

    return mult


if __name__ == '__main__':
    while True:
        try:
            option = int(input('Which task you want to see?\n'
                               '1. Welcome to Python\n'
                               '2. Python Art\n'
                               '3. Title\n'
                               '4. Formatted input of money\n'
                               '5. Carpet Designer\n'
                               '6. Multiplication of number\'s digits\n'
                               '0. Quit\n'
                               'Enter your choice: '))

            match option:
                case 1:
                    name, last_name = input('\nEnter your name and last name: ').split(' ')[:2]
                    result = welcome_to_python(name, last_name)
                    print(result, end='\n\n')
                case 2:
                    c = input('\nEnter any character: ')
                    if len(c) > 1:
                        raise ValueError('\'c\' must contain only 1 symbol')
                    fig_ths = int(input('Enter thickness of your figure: '))
                    python_art(c, fig_ths)
                case 3:
                    text = input('\nEnter any text: ')
                    result = title(text)
                    print(result, end='\n\n')
                case 4:
                    money = float(input('\nEnter any sum of money: '))
                    result = formatted_money(money)
                    print(result, end='\n\n')
                case 5:
                    carpet_width = int(input('\nEnter your desired carpet width: '))
                    carpet_designer(carpet_width)
                case 6:
                    num = int(input('\nEnter any number: '))
                    result = multiply_digits(num)
                    print(result, end='\n\n')
                case 0:
                    print('\nGoodbye!')
                    break
                case _:
                    print('\nUndefined option\n')
        except ValueError as error:
            print('\nError (%s) has occurred, try again' % error)
