# funckja sprawdzajaca czy slowo przeczytane od tylu jest takie same (palindrom)
def Is_palidrome(text):
    # zdanie bez spacji, zamiana spacji na znak pusty
    text = text.replace(" ", "").lower()
    # początkowa litera słowa
    i = 0
    # ostatnia litera słowa
    j = len(text) - 1
    # założenie że słowo jest palidromem
    palindrome = True
    # pętla dopóki i będzie równe j
    while i < j:
        # sprawdzenie czy znaki są różne
        if text[i] != text[j]:
            # nie jest palindromem
            palindrome = False
            # przerwanie pętli
            break
        # następna litera
        i += 1
        # następna litera od tyłu
        j -= 1
    # sprawdzenie wartości palidromu
    if palindrome:
        # jest palindromem
        return True
    else:
        # nie jest palindromem
        return False
