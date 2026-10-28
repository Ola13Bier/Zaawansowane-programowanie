def Is_palidrome(text):
    i = 0
    j = len(text) - 1
    palindrome = False
    while i < j:
        if text[i] != text[j]:
            palindrome = True
            break
        i += 1
        j -= 1

    if palindrome:
        return True
    else:
        return False
