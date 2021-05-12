# https://github.com/uvsq22006204/CryptoProjet #
## gui pas fini ##

def ROT(text, n, k=1):
    n = int(n)
    res = ""
    for line in text:
            line.strip()
            for c in line:
                if c in alpha:
                   i = alpha.index(c)
                   j = (i + k*n)%26
                   res += alpha[j]
                else: res += c
    return res


def SUBSTITUTION(text, beta, k=1):
    if k == 1: delta = dict(zip(alpha, list(beta)))
    if k == -1: delta = dict(zip(beta, list(alpha)))
    res = ""
    for line in text:
        for c in line:
            if c in alpha:
                res += delta[c]
            else: res += c
    return res


def VIGENERE(text, pw, k=1):
    res = ""
    i = 0
    for line in text:
        line.strip()
        for c in line:
            if c in alpha:
                temp = alpha.index(c)
                temp -= (alpha.index(pw[i%len(pw)]) * k)
                res += alpha[temp%26]
            else: res += c
            i += 1
    return res


def count_letters(text):
    """Count every letters in a text"""
    freq_dict = {}
    for c in alpha:
        n = 0
        for line in text:
            if c in line:
                n += line.count(c)
        freq_dict[c] = n
    return freq_dict


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
    
    pw_len_dict = {}
    for n in range(mini, maxi+1):
        list_res = period_split(line, n)
        IC = 0
        
        for res in list_res:
            IC += get_IC([res])
        
        pw_len_dict[n] = IC/len(list_res)
    return pw_len_dict


def divide(line, n):
    """Divide a line into n column"""
    for i in range(len(line) // n):
        print(line[i*n:(i+1)*n])


def mirror(text, x_axis=False, y_axis=False):
    x, y = 1, 1
    if x_axis: x = -1
    if y_axis: y = -1
    return [line[::y] for line in text[::x]]


def brute_force(text):
    sample = text[0][:15]
    
    bf_res_dict = {}
    for n in range(1, 26):
        res = ROT([sample], n)
        bf_res_dict[n] = res
    return bf_res_dict


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
    text_1, text_2, text_3, text_4, text_5 = get_texts()
    text_4 = mirror(text_4, True, True)
    
    ROT(text_1, 1)
    SUBSTITUTION(text_2, "z-dn-ml-s-ihgar-p-o-tcfeu-")
    VIGENERE(text_3, "clez")
    VIGENERE(text_4, "bravez")
    
    console()


alpha = list("abcdefghijklmnopqrstuvwxyz")

if __name__ == '__main__': main()
