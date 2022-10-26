from random import randint


def average(*args) -> float:
    return sum(args) / len(args)


def divide(dividend: int, divider: int) -> list[int]:
    return [dividend // divider, dividend % divider]


def round_number(number: float, option: int) -> str:
    match option:
        case 1:
            return '%.2f' % number
        case 2:
            return '%.f' % number
        case 3:
            return f'{number:011}'
        case _:
            raise ValueError


def reverse(number: int) -> int:
    sign = number // abs(number)
    digit_list = list(map(str, str(abs(number))))

    if len(digit_list) == 1:
        return number

    digit_list.reverse()

    return sign * int(''.join(digit_list))


def reverse_int32(number: int) -> int:
    revs = reverse(number)
    return revs if abs(number) <= 2**31 else 0


def main():
    num1, num2, num3 = [randint(0, 100) for i in range(3)]
    result = average(num1, num2, num3)
    print(result)

    to_div, div = list(map(int, input('Enter a dividend and a divider: ').split(' ')))
    result = divide(to_div, div)
    print(result)

    to_round = float(input('Enter any float number: '))
    print(round_number(to_round, 1), round_number(to_round, 2), round_number(to_round, 3))

    to_rev = int(input('Enter a number you want to reverse: '))
    result = reverse(to_rev)
    print(result)

    to_rev = int(input('Enter a number you want to reverse: '))
    result = reverse_int32(to_rev)
    print(result)


if __name__ == '__main__':
    main()

