alph=list("abcdefghijklmnopqrstvuwxyz")

def SwapSymbol(symbol,n):
    if symbol.islower():
        idx = alph.index(symbol)
        new_idx = (idx + n) % len(alph)
        new_symbol = alph[new_idx]
    else:
        symbol = symbol.lower()
        idx = alph.index(symbol)
        new_idx = (idx + n) % len(alph)
        new_symbol = alph[new_idx].upper()
    return new_symbol

def alg(string):
    i=0
    while i<len(string):
         j=i
         if string[i].isalpha():
             countChar=0
             while string[j].isalpha():
                 countChar=countChar+1
                 j=j+1
             j=i
             while string[j].isalpha():
                string=string[:j]+SwapSymbol(string[j],countChar)+string[j+1:]
                j=j+1
             i=j
         else:
             i=i+1
    return string

def main():
    string = "Day, mice. \"Year\" is a mistake#"
    print(alg(string))
main()