#### Imports et définition des variables globales
"""Module pour encoder une chaîne de caractères selon un algorithme"""
# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    # Initialisation
    caractere = [s[0]]
    occurences = [1]
    for elem in s[1:]:
        if elem == caractere[-1]:
            occurences[-1] += 1
        else:
            caractere.append(elem)
            occurences.append(1)
    return list(zip(caractere, occurences))


def artcode_r(s):
    """retourne la liste de tuples un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    first_char = s[0]
    compteur = 1
    while compteur < len(s) and s[compteur] == first_char:
        compteur += 1
    return [(first_char, compteur)] + artcode_r(s[compteur:])

#### Fonction principale
def main():
    """fonction principale pour tester les deux algorithmes"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))
if __name__ == "__main__":
    main()
