import sys
import random

def guessNumber():
    print('Zgadnij jaką liczbę mam na myśli od 1 do 20.')
    print('Masz tylko 4 próby!')
    guessNum = random.randint(1, 20)
    count = 4
    i = 0

    while count > 0:
        try:
            tryNum = int(input('Twoja propozycja: '))
            if tryNum < 1 or tryNum > 20:
                print("Liczba musi być w zakresie od 1 do 20. Spróbuj ponownie.")
                continue
            if tryNum < guessNum:
                print('Myślę o większej liczbie.')
                count -= 1
                i += 1
            elif tryNum > guessNum:
                print('Myślę o mniejszej liczbie.')
                count -= 1
                i += 1
            else:
                print(f'Gratulacje! Liczba {guessNum} jest właśnie tą, o której myślałem!')
                print(f'Udało Ci się ją odgadnąć w {i + 1} próbach!')
                break
        except ValueError:
            print("Proszę podać prawidłową liczbę.")
            continue

        if count == 0:
            print(f'Przegrana! Prawidłowa liczba to {guessNum}.')

    menu()

def menu():
    print('Czy chcesz zagrać w grę "Odgadnij liczbę"? [Y/N]')
    choice = input()
    if choice.lower() == 'y':
        guessNumber()
    elif choice.lower() == 'n':
        sys.exit()
    else:
        print('\nBłąd wyboru, wprowadź Y dla "TAK" lub N dla "Nie".\n')
        menu()

menu()

    
        

        