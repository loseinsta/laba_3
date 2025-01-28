file = open('input.txt', 'r')
data = file.read()

numbers = data.split()

num_to_word = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

max_number = None

for num_str in numbers:
    try:
        number = int(num_str)
        if number % 2 == 0:  # Проверка, четное ли число
            num_str = str(number)
            if len(num_str) == 1:
                swapped_number = number
            else:
                swapped_number = int(num_str[-1] + num_str[1:-1] + num_str[0])

            print(swapped_number)

            if max_number is None or swapped_number > max_number:
                max_number = swapped_number
    except ValueError:
        continue

if max_number is not None:
    max_number_str = str(max_number)
    max_number_words = ' '.join(num_to_word[digit] for digit in max_number_str)
    print(max_number_words)