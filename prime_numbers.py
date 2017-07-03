"""module for generating prime numbers between 0 and n"""


def prime_numbers(number):
    """function to generate prime numbers between 0 and n."""

    prime_number_list = []

    if number in (0, 1):
        return "0 or 1 are not prime numbers."

    if number < 2:
        return "integers less than 2 cannot be prime numbers"

    if not isinstance(number, int):
        return "only integers are allowed."

    for i in range(2, number + 1):
        if i > 1:
            for x in range(2, i):
                if (i % x) == 0:
                    break
            else:
                prime_number_list.append(i)
    return prime_number_list
