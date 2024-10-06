"""
Encoder une chaîne de caractères
selon un algorithme itératif ou récursif.
"""

#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici

    char_list=[]
    occurrence_list=[]
    char_list.append(s[0])
    occurrence_list.append(1)
    cmpt=0
    x=1
    d=0
    while s[x:]!="":
        if cmpt==len(s):
            break
        if s[x]==s[x-1]:
            occurrence_list[d]=occurrence_list[d]+1
            cmpt=cmpt+1
            x=x+1
        else:
            char_list.append(s[x])
            occurrence_list.append(1)
            cmpt=cmpt+1
            x=x+1
            d=d+1

    return list(zip(char_list, occurrence_list))

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
    en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # cas de base
    temp=[]
    n=len(s)
    buf=255

    if n > buf:
        s1=artcode_r(s[:buf])
        s2=artcode_r(s[buf:])


        if s1 and s2 and s1[-1][0]==s2[0][0]:
            s1[-1]=(s1[-1][0],s1[-1][1]+s2[0][1])
            s2=s2[1:]
        return s1 + s2
    # recherche nombre de caractères identiques au premier
    if n == 1:
        return [(s, 1)]
    c = s[0]
    temp = artcode_r(s[1:])

    if temp[0][0] == c:
        return [(c, temp[0][1] + 1)] + temp[1:]
    return [(c, 1)] + temp
    # appel récursif
#### Fonction principale


def main():
    """Fonction principale pour tester les algorithmes d'encodage itératif et récursif."""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
