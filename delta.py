
## kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd.
## le prochain fichier aura un code par substitution alphabetique: chaque lettre est remplacee par une autre. utiliser la frequence des lettres pour decoder le message.

## gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi.
## le prochain fichier est code par un mot de passe de taille inconnue et contient l'indice. les lettres du mot de passe permettent de decaler les lettres du message original modulo 26. seules les lettres de a a ? sont chiffrees.

## dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?
## bravo a l'aide de l'indice vous avez reussi a casser ce code et a finir ce devoir. le dernier texte est pour les braves, regardez vous dans un miroir, en etes vous un ?

## Tfmcxc dcd lgaqnbdccqbec, nbhc rnlk bvaiblhaé yk sceegga cxzrv, garac bdrawmhmrzwc o ay rfaelbvfcefhx q'yeckrv hrg. Sblkb alcdczvd ewv adaq klckb jlraoeccbé ewbc wc ccoxrqe ck ynuotcé.


def ROT(text, n):
    res = ""
    for line in text:
            line.strip()
            for c in line:
                if c in alpha:
                   i = alpha.index(c)
                   res += alpha[(i + n)%26]
                else: res += c
    print("\nROT:\n", res)


def SUBSTITUTION(text, beta):
    delta = dict(zip(alpha, list(beta)))
    res = ""
    for line in text:
        for c in line:
            if c in alpha:
                res += delta[c]
            else: res += c
    print("\nSubstitution:\n", res)


def VIGENERE(text, pw):
    res = ""
    i = 0
    for line in text:
        line.strip()
        for c in line:
            if c in alpha:
                temp = 26 + alpha.index(c)
                temp -= alpha.index(pw[i%len(pw)])
                res += alpha[temp%26]
            else: res += c
            i += 1
    print("\nVigenere:\n", res)


def count_letters(text):
    """Count every letters in a text"""
    for c in alpha:
        n = 0
        for line in text:
            if c in line:
                n += line.count(c)
        print(c, ": ", n)


def get_IC(text):
    """Get the index of coincidence of a text"""
    num = 0
    N = 0
    for line in text:
        for c in alpha:
            n = line.count(c)
            num += n * (n - 1)
            N += n
    if N:
        return num / (N * (N - 1))


def period_split(line, n):
    return [line[i::n] for i in range(n)]


def text_to_line(text):
    return "".join(text)


def pw_length(line, mini, maxi):
    """Give average IC for every given size of the password"""
    if isinstance(line, list):
        line = text_to_line(line)
    
    for n in range(mini, maxi+1):
        list_res = period_split(line, n)
        IC = 0
        
        for res in list_res:
            IC += get_IC([res])
        
        print(n, ": ", IC/len(list_res))


def divide(line, n):
    """Divide a line into n column"""
    for i in range(len(line) // n):
        print(line[i*n:(i+1)*n])


def mirror(text, x_axis, y_axis):
    x, y = 1, 1
    if x_axis: x = -1
    if y_axis: y = -1
    return [line[::y] for line in text[::x]]


def console():
    while True: # 'exit()' to quit
        try: exec(input("~"))
        except Exception as e: print(e)


def get_texts():
    with open("texte 1") as file: text_1 = [file.readline()]
    with open("texte 2") as file: text_2 = [file.readline()]
    with open("texte 3") as file: text_3 = [file.readline()]
    with open("texte 4") as file: text_4 = file.readlines()
    with open("texte 5") as file: text_5 = [file.readline()]
    return text_1, text_2, text_3, text_4, text_5


def main():
    global alpha, text_1, text_2, text_3, text_4, text_5
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    text_1, text_2, text_3, text_4, text_5 = get_texts()
    text_4 = mirror(text_4, True, True)
    
    ROT(text_1, 1)
    SUBSTITUTION(text_2, "z-dn-ml-s-ihgar-p-o-tcfeu-")
    VIGENERE(text_3, "clez")
    VIGENERE(text_4, "bravez")
    
    console()


if __name__ == '__main__': main()
