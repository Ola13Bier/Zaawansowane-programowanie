# czy lista zawiera wartość parametru
def CzyListaZawieraParametr(tab: list, i: int):
    # ile razy występuje dany paramert w liscie
    ans = tab.count(i)
    # wystepowanie jest rowne 0
    if ans == 0:
        # nie zawiera
        return False
    # występuje chociaż raz
    else:
        # zawiera
        return True
