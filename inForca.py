import random
from words import words
from visualForca import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def restard():
    resp = input('Precione a tecla <F> para continuar jogando,'
          'ou para sair a tecla <G> : ').upper()
    if resp == "G":
        exit()
    if restard == "F":
        hangman()
    return



def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7


    while len(word_letters) > 0 and lives > 0:
        print('Você tem', lives, 'vidas restantes e usou estas letras: ', ' '.join(used_letters))


        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Palavra Atual: ', ' '.join(word_list))

        user_letter = input('Advinhe uma letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1
                print('\nSua letra:', user_letter, 'não está na palavra.')

        elif user_letter in used_letters:
            print('\nVocê já usou essa letra. Adivinhe outra letra.')

        else:
            print('\nEssa não é uma "letra" válida.')


    if lives == 0:
        print(lives_visual_dict[lives])
        print('ERROU!!! Você se fudeu. A palavra era:', word)
        print(input(restard()))
    else:
        print(lives_visual_dict)
        print('NICE! Você advinhou a palavra', word, '!!')
        print(input(restard()))


while restard() == hangman():
    if __name__ == '__main__':
        hangman()
