def fizzbuzz(number: int) -> str:
    res = ''
    if number % 3 == 0:
        res += 'Fizz'
    if number % 5 == 0:
        res += (' ' if len(res) else '') + "Buzz"

    if not len(res):
        return str(number)
    return res


def num_estimation(number: int) -> str:
    if number % 2 != 0:
        return 'Bad'
    if number <= 5:
        return 'Not bad'
    if number <= 20:
        return 'So-so'
    return 'Good'


def sequence(number: int) -> str:
    return ''.join([str(i) for i in range(1, number + 1)])


def secret_message(message: str) -> str:
    return ''.join([(i if i.isupper() else '') for i in message])


def three_words(string: str) -> bool:
    split_string = string.split()
    if len(split_string) < 3:
        return False

    amount_between = []
    word_counter = 0

    for index in range(len(split_string)):
        if split_string[index].isnumeric():
            amount_between.append(word_counter)
            word_counter = 0
            continue
        word_counter += 1

    for item in amount_between:
        if item >= 3:
            return True

    return False


def right_to_left(seq: list[str]) -> list[str]:
    result_seq = seq.copy()

    for index in range(len(result_seq)):
        while 'right' in result_seq[index]:
            result_seq[index] = result_seq[index].replace('right', 'left')

    return result_seq


if __name__ == '__main__':
    while True:
        try:
            option = int(input('Which task you want to see?\n'
                               '1. Fizz Buzz\n'
                               '2. Estimation of a number\n'
                               '3. Sequence\n'
                               '4. Secret Message\n'
                               '5. Is there three words in a row\n'
                               '6. Change "right" substring to "left"\n'
                               '0. Quit\n'
                               'Enter your choice: '))

            match option:
                case 1:
                    num = int(input('Enter any number: '))
                    result = fizzbuzz(num)
                    print(result, end='\n\n')
                case 2:
                    num = int(input('Enter any number: '))
                    result = num_estimation(num)
                    print(result)
                case 3:
                    num = int(input('Enter any number: '))
                    result = sequence(num)
                    print(result, end='\n\n')
                case 4:
                    string = input('Enter string with secret message: ')
                    result = secret_message(string)
                    print(result, end='\n\n')
                case 5:
                    string = input('Enter any string: ')
                    result = three_words(string)
                    print('Yes' if result else 'No', end='\n\n')
                case 6:
                    list_of_strings = ['alright lefties won', 'help', 'right right right']
                    result = right_to_left(list_of_strings)
                    print(result, end='\n\n')
                case 0:
                    print('\nGoodbye!')
                    break
                case _:
                    print('\nUndefined option: Try again\n')
        except ValueError as error:
            print('\nError (%s) has occurred, try again' % error)
