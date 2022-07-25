from random import choice

# This program displays a quote from a list of quotes
# stored locally as 'quotes.txt'

def get_quote():
    try:
        with open('quotes.txt', 'r', encoding='utf8') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("#"):
                    lines.remove(line)
            num = choice(range(len(lines)))
            return lines[num]
    except IOError as e:
        return e


def main():
    print(get_quote(), sep='')
    input()


main()