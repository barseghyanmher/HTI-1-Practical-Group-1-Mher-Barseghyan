from words import get_a_word


def start():
    step = 0
    word = get_a_word().upper()
    letters = set(word)
    tries = set()

    while step < 5:
        if tries.issuperset(letters):
            for letter in word:
                print(f' {letter} ', end='')
            print()
            print('You won the game.')
            break

        print(f'Guess the word. {5 - step} mistakes left.')

        for letter in word:
            if letter in tries:
                print(f' {letter} ', end='')
            else:
                print(' _ ', end='')
        print()

        letter = input('Guess a letter.').upper()
        print()
        if letter not in letters:
            step += 1
        tries.add(letter)
    if step == 5:

        print(f"I'm sorry but you lose, the word is a {word}")

start()
